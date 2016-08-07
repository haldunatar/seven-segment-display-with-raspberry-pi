execfile("/home/pi/Desktop/ssd/settings/gpioSetup.py")

### To light 4 we need the b, c, f, g segments.

def four():
     ### set the segments on 
     GPIO.output(segment['b'], 1)
     GPIO.output(segment['c'], 1)
     GPIO.output(segment['f'], 1)
     GPIO.output(segment['g'], 1)

     ### wait for one second
     time.sleep(1)
     
     ### set the segments off 
     GPIO.output(segment['b'], 0)
     GPIO.output(segment['c'], 0)
     GPIO.output(segment['f'], 0)
     GPIO.output(segment['g'], 0)
