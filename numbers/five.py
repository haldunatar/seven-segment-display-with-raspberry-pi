execfile("/home/pi/Desktop/ssd/settings/gpioSetup.py")

### To light 5 we need the a, c, d, f, g segments.

def five():
     ### set the segments on
     GPIO.output(segment['a'], 1)
     GPIO.output(segment['c'], 1)
     GPIO.output(segment['d'], 1)
     GPIO.output(segment['f'], 1)
     GPIO.output(segment['g'], 1)

     ### wait for one second
     time.sleep(1)
     
     ### set the segments off
     GPIO.output(segment['a'], 0)
     GPIO.output(segment['c'], 0)
     GPIO.output(segment['d'], 0)
     GPIO.output(segment['f'], 0)
     GPIO.output(segment['g'], 0)
