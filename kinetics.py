import RPi.GPIO as GPIO
import time

# Define pins
FWD_PIN = 16
BACK_PIN = 19

# Initialize GPIO mode once at the beginning
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setup():
    """Initialize the GPIO pins."""
    GPIO.setup(FWD_PIN, GPIO.OUT)
    GPIO.setup(BACK_PIN, GPIO.OUT)
    # Ensure pins start in LOW state
    GPIO.output(FWD_PIN, GPIO.LOW)
    GPIO.output(BACK_PIN, GPIO.LOW)

def cleanup():
    """Clean up GPIO pins."""
    GPIO.cleanup([FWD_PIN, BACK_PIN])

def forward(duration=1.0):
    """Move forward for the specified duration in seconds."""
    # Clean up pins first
    cleanup()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # Set up and activate forward pin
    GPIO.setup(FWD_PIN, GPIO.OUT)
    GPIO.output(FWD_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    GPIO.output(FWD_PIN, GPIO.LOW)
    cleanup()

def backward(duration=1.0):
    """Move backward for the specified duration in seconds."""
    # Clean up pins first
    cleanup()
    
    # Re-initialize GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # Set up and activate backward pin
    GPIO.setup(BACK_PIN, GPIO.OUT)
    GPIO.output(BACK_PIN, GPIO.HIGH)
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    GPIO.output(BACK_PIN, GPIO.LOW)
    cleanup()

def stop():
    """Stop all movement by cleaning up pins."""
    # Set pins to LOW then clean up
    try:
        GPIO.output(FWD_PIN, GPIO.LOW)
        GPIO.output(BACK_PIN, GPIO.LOW)
    except:
        pass
    cleanup()

# Test bench
if __name__ == "__main__":
    try:
        print("RC Movement Test Bench")
        print("----------------------")
        
        print("Setting up pins...")
        setup()
        time.sleep(1.0)
        
        print("Testing forward movement for 2 seconds...")
        forward(2.0)
        time.sleep(1.0)
        
        print("Testing backward movement for 2 seconds...")
        backward(2.0)
        time.sleep(1.0)
        
        print("Testing sequence: forward 1s, stop 1s, backward 1s...")
        forward(1.0)
        time.sleep(1.0)
        backward(1.0)
        
        print("Test complete.")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    finally:
        print("Cleaning up pins...")
        stop()