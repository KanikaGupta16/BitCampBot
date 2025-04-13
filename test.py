import RPi.GPIO as GPIO
import time

# Define all pins
FWD_BACK_COMMON = 17
FWD_PIN = 16
BACK_PIN = 19
LEFT_RIGHT_COMMON = 18
RIGHT_PIN = 20
LEFT_PIN = 26

# Initialize GPIO mode once at the beginning
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setup_pin(pin, initial_state=GPIO.LOW):
    """Set up a single pin as output with initial state."""
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, initial_state)

def cleanup_specific_pins(pins):
    """Clean up specific GPIO pins."""
    for pin in pins:
        GPIO.cleanup(pin)

def cleanup_all():
    """Clean up all GPIO pins."""
    GPIO.cleanup()

def forward_right(duration=1.0):
    """Move forward for the specified duration in seconds."""
    # Clean up all pins first
    cleanup_all()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # Set up only the pins needed for forward movement
    setup_pin(FWD_BACK_COMMON, GPIO.HIGH)
    setup_pin(FWD_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def backward(duration=1.0):
    """
    Move backward and left for the specified duration in seconds.
    Based on observations, this is achieved with backward + right pins.
    """
    # Clean up all pins first
    cleanup_all()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # According to the test results, backward + right pins results in backward left
    setup_pin(FWD_BACK_COMMON, GPIO.HIGH)
    setup_pin(BACK_PIN, GPIO.HIGH)
    setup_pin(LEFT_PIN, GPIO.HIGH)
    setup_pin(LEFT_RIGHT_COMMON, GPIO.LOW)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()


def forward(duration=1.0):
    """
    Move forward and left for the specified duration in seconds.
    Based on observations, this is achieved with forward + right pins.
    """
    # Clean up all pins first
    cleanup_all()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # According to the test results, forward + right pins results in forward left
    setup_pin(FWD_BACK_COMMON, GPIO.HIGH)
    setup_pin(FWD_PIN, GPIO.HIGH)
    setup_pin(LEFT_PIN, GPIO.HIGH)
    setup_pin(LEFT_RIGHT_COMMON, GPIO.LOW)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def backward_left(duration=1.0):
    """
    Move backward and right for the specified duration in seconds.
    Based on observations, this is achieved with just backward pins.
    """
    # Clean up all pins first
    cleanup_all()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # According to the test results, backward alone results in backward right
    setup_pin(FWD_BACK_COMMON, GPIO.HIGH)
    setup_pin(BACK_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def backward(duration=1.0):
    """
    Move backward and right for the specified duration in seconds.
    Based on observations, this is achieved with just backward pins.
    """
    # Clean up all pins first
    cleanup_all()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # According to the test results, backward alone results in backward right
    setup_pin(FWD_BACK_COMMON, GPIO.HIGH)
    setup_pin(BACK_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def stop():
    """Stop all movement by cleaning up all pins."""
    cleanup_all()

# Example usage
if __name__ == "__main__":
    try:
        print("RC Movement Demo")
        
        print("Moving forward")
        forward(2.0)
        time.sleep(1.0)
        
        print("Moving forward-right")
        forward_right(2.0)
        time.sleep(1.0)
        
        print("Moving backward")
        backward(2.0)
        time.sleep(1.0)
        
        print("Moving backward-left")
        backward_left(2.0)
        time.sleep(1.0)
        
        
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        stop()