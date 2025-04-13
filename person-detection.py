import cv2
import numpy as np
import time
from gpiozero import Robot
import kinetics as c

def detect_person(frame):
    # Initialize HOG descriptor for person detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Detect people in the frame
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8),
                                         padding=(4, 4), scale=1.05)
    
    # Return the largest bounding box (closest person)
    if len(boxes) > 0:
        largest_box = max(boxes, key=lambda box: box[2] * box[3])
        return largest_box
    return None

def setup_camera(camera_id=0, width=640, height=480):
    # Initialize the camera
    camera = cv2.VideoCapture(camera_id)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return camera

def setup_motors(left_pins=(17, 18), right_pins=(22, 23)):
    # Initialize the robot with the GPIO pins for left and right motors
    robot = Robot(left=left_pins, right=right_pins)
    return robot

def move_forward(robot, speed=1.0):
    c.forward(0.3)
    time.sleep(2)

def move_backward(robot, speed=1.0):
    print("backward")
    #robot.backward(speed)
    c.backward(0.3)
    time.sleep(2)

def turn_left(robot, speed=0.5):
    #robot.left(speed)
    pass

def turn_right(robot, speed=0.5):
    #robot.right(speed)
    pass

def stop(robot):
    robot.stop()

def follow_person(camera, robot, target_width=100, min_distance=80, max_distance=120):
    """
    Follow the detected person while maintaining a specific distance range.
    
    :param camera: OpenCV VideoCapture object
    :param robot: gpiozero Robot object
    :param target_width: Ideal width of the person in pixels
    :param min_distance: Minimum acceptable distance from the person
    :param max_distance: Maximum acceptable distance from the person
    :return: Boolean indicating if tracking was successful
    """
    # Read a frame from the camera
    ret, frame = camera.read()
    if not ret:
        return False
    
    # Detect the person in the frame
    person_box = detect_person(frame)
    
    if person_box is not None:
        x, y, w, h = person_box
        frame_center = frame.shape[1] // 2
        person_center = x + (w // 2)
        
        # Calculate how far the person is from the center
        center_diff = person_center - frame_center
        
        # Decide how to move based on the person's position and size
        if w < min_distance:  # Person is too small (too far away)
            # Move forward at a speed proportional to how far away the person is
            forward_speed = min(1.0, (min_distance - w) / min_distance)
            move_forward(robot, forward_speed)
            print(f"Moving forward: speed = {forward_speed}")
        
        elif w > max_distance:  # Person is too large (too close)
            # Move backward at a speed proportional to how close the person is
            backward_speed = min(1.0, (w - max_distance) / max_distance)
            move_backward(robot, backward_speed)
            print(f"Moving backward: speed = {backward_speed}")
        
        elif abs(center_diff) > 50:  # Person is not centered
            # Adjust rotation speed based on how far from center
            turn_speed = min(1.0, abs(center_diff) / frame.shape[1])
            if center_diff > 0:
                turn_right(robot, turn_speed)
                print(f"Turning right: speed = {turn_speed}")
            else:
                turn_left(robot, turn_speed)
                print(f"Turning left: speed = {turn_speed}")
        
        else:  # Person is in a good position
            stop(robot)
            print("Maintaining position")
    
    else:
        # No person detected, stop moving
        stop(robot)
        print("No person detected")
    
    return True

def main():
    # Initialize the camera and robot
    camera = setup_camera()
    robot = setup_motors()
    
    try:
        while True:
            # Follow the person
            if not follow_person(camera, robot):
                break
            
            # Add a small delay
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        print("Program stopped by user")
    
    finally:
        # Clean up
        camera.release()
        stop(robot)

if __name__ == "__main__":
    main()