import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# List of all pins to clear
pins = [16, 17, 18, 19, 20, 26]  # Add any other pins you've been using

def cleanup_all_pins():
    """Clean up all GPIO pins"""
    print("Cleaning up all GPIO pins...")
    
    # First try to set them all as outputs and set LOW
    for pin in pins:
        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            print(f"Pin {pin} set to LOW")
        except:
            print(f"Could not set pin {pin} to LOW")
    
    # Then do a proper cleanup
    GPIO.cleanup()
    print("All pins cleaned up")

if __name__ == "__main__":
    cleanup_all_pins()
    print("Done. All pins should now be in their default state.")