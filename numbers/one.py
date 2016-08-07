execfile("/home/pi/Desktop/ssd/settings/gpioSetup.py")

### To light 1 we need the b, c segments.

def one():
     ### set the segments on
     GPIO.output(segment['b'], 1)
     GPIO.output(segment['c'], 1)

     ### wait for one second
     time.sleep(1)
     
     ### set the segments off
     GPIO.output(segment['b'], 0)
     GPIO.output(segment['c'], 0)
