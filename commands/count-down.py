execfile("/home/pi/Desktop/ssd/numbers/one.py")
execfile("/home/pi/Desktop/ssd/numbers/two.py")
execfile("/home/pi/Desktop/ssd/numbers/three.py")
execfile("/home/pi/Desktop/ssd/numbers/four.py")
execfile("/home/pi/Desktop/ssd/numbers/five.py")
execfile("/home/pi/Desktop/ssd/numbers/six.py")
execfile("/home/pi/Desktop/ssd/numbers/seven.py")
execfile("/home/pi/Desktop/ssd/numbers/eight.py")
execfile("/home/pi/Desktop/ssd/numbers/nine.py")
execfile("/home/pi/Desktop/ssd/numbers/zero.py")
import unittest

countDownNumbers = [
    'nine',
    'eight',
    'seven',
    'six',
    'five',
    'four',
    'three',
    'two',
    'one',
    'zero'
];

def countDown():
    for num in countDownNumbers:
        globals()[num]()

### Display Countdown
countDown()