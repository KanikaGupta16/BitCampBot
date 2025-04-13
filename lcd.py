from RPLCD.i2c import CharLCD
import time

# Try with the address that appeared in your i2cdetect
try:
    # Using PCF8574 expander
    lcd = CharLCD('PCF8574', 0x62, port=1, backlight_enabled=True)
    print("Successfully connected to LCD at 0x62 with PCF8574")
    time.sleep(5)  # Keep backlight on for 5 seconds
    
    # Turn backlight off
    lcd.backlight_enabled = False
    print("Turned backlight off")
    time.sleep(2)
    
    # Turn backlight on again
    lcd.backlight_enabled = True
    print("Turned backlight on")
    time.sleep(2)
    
except Exception as e:
    print(f"Error with PCF8574 at 0x62: {e}")
    
    try:
        # Try with MCP23008 expander
        lcd = CharLCD('MCP23008', 0x62, port=1, backlight_enabled=True)
        print("Successfully connected to LCD at 0x62 with MCP23008")
        time.sleep(5)
        
        # Turn backlight off
        lcd.backlight_enabled = False
        print("Turned backlight off")
        time.sleep(2)
        
        # Turn backlight on again
        lcd.backlight_enabled = True
        print("Turned backlight on")
        
    except Exception as e:
        print(f"Error with MCP23008 at 0x62: {e}")