import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### Segments will be set on GPIO such as:

segment = {
    'a': 9,
    'b': 10,
    'c': 4,
    'd': 17,
    'e': 23,
    'f': 11,
    'g': 5,
    'dot': 22
}
 
GPIO.setup(segment['a'], GPIO.OUT)
GPIO.setup(segment['b'] , GPIO.OUT)
GPIO.setup(segment['c'], GPIO.OUT)
GPIO.setup(segment['d'], GPIO.OUT)
GPIO.setup(segment['e'], GPIO.OUT)
GPIO.setup(segment['f'], GPIO.OUT)
GPIO.setup(segment['g'], GPIO.OUT)
GPIO.setup(segment['dot'], GPIO.OUT) 
