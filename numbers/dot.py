execfile("/home/pi/Desktop/ssd/settings/gpioSetup.py")

### To light . we need the dot segment.

def dot():
     ### set the segments on
     GPIO.output(segment['dot'], 1) 

     ### wait for one second
     time.sleep(1)
     
     ### set the segments off
     GPIO.output(segment['dot'], 0) 
