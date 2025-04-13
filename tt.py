import RPi.GPIO as GPIO
import time

def setup_pin(pin, initial_state=GPIO.LOW):
    """Set up a single pin as output with initial state."""
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, initial_state)

def cleanup_all():
    """Clean up all GPIO pins."""
    GPIO.cleanup()

def forward(duration=1.0):
    """Move forward for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up only the pins needed for forward movement
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(16, GPIO.HIGH)  # FWD_PIN
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def backward(duration=1.0):
    """Move backward for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up only the pins needed for backward movement
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(19, GPIO.HIGH)  # BACK_PIN
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def left(duration=1.0):
    """Turn left for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up only the pins needed for left movement
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    # LEFT_RIGHT_COMMON (18) not connected for left
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def right(duration=1.0):
    """Turn right for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up only the pins needed for right movement
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    setup_pin(18, GPIO.LOW)   # LEFT_RIGHT_COMMON
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

# FIXED FUNCTION - Changed to properly activate both forward and left
def forward_left(duration=1.0):
    """Move forward and left for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up forward pins
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(16, GPIO.HIGH)  # FWD_PIN
    
    # Set up left pins
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    # Make sure LEFT_RIGHT_COMMON is not LOW (per your feedback)
    # Based on "26 HIGH and 18 none is left and backward" from your description
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def forward_right(duration=1.0):
    """Move forward and right for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up forward pins
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(16, GPIO.HIGH)  # FWD_PIN
    
    # Set up right pins
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    setup_pin(18, GPIO.LOW)   # LEFT_RIGHT_COMMON
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

def backward_left(duration=1.0):
    """Move backward and left for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up backward pins
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(19, GPIO.HIGH)  # BACK_PIN
    
    # Set up left pins
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    # LEFT_RIGHT_COMMON (18) not connected for left
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

# FIXED FUNCTION - Changed to properly activate both backward and right
def backward_right(duration=1.0):
    """Move backward and right for the specified duration in seconds."""
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set up backward pins - these need to be activated first
    setup_pin(17, GPIO.HIGH)  # FWD_BACK_COMMON
    setup_pin(19, GPIO.HIGH)  # BACK_PIN
    
    # Set up right pins - make sure these are set correctly
    setup_pin(26, GPIO.HIGH)  # LEFT_PIN
    setup_pin(18, GPIO.LOW)   # LEFT_RIGHT_COMMON
    
    # Wait for the specified duration
    time.sleep(duration)
    
    # Clean up
    cleanup_all()

# Example usage
if __name__ == "__main__":
    try:
        print("Testing each movement for 2 seconds")
        
        print("Testing forward")
        forward(2.0)
        time.sleep(1.0)  # Wait a second between tests
        
        print("Testing forward_left")
        forward_left(2.0)
        time.sleep(1.0)
        
        print("Testing forward_right")
        forward_right(2.0)
        time.sleep(1.0)
        
        print("Testing backward")
        backward(2.0)
        time.sleep(1.0)
        
        print("Testing backward_left")
        backward_left(2.0)
        time.sleep(1.0)
        
        print("Testing backward_right")
        backward_right(2.0)
        
    except KeyboardInterrupt:
        print("Program stopped by user")
        cleanup_all()