import kinetics as c
import time



try:
    print("f")
    c.forward(0.3)
    time.sleep(2)


    print("b")
    c.backward(0.1)
    time.sleep(1)

    c.stop()

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    c.stop()
