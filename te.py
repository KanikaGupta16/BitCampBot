import RPi.GPIO as GPIO
import time

LOW_PIN = 26  # This pin will be set LOW

# for Back 19 are high
# for FWD 16 are high 
#Cleanup all pins for stopping 


# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins as outputs
GPIO.setup(LOW_PIN, GPIO.OUT)



try:
    # Set first pin HIGH
    GPIO.output(LOW_PIN, GPIO.HIGH)
    print(f"Pin {LOW_PIN} set to HIGH")
    
    # Keep the program running to maintain the pin states
    print("Press CTRL+C to exit")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    
finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
    print("GPIO cleaned up")