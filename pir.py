
import RPi.GPIO as GPIO
import time
import dht11
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
pirno =14


def call(pirno):
    while True:
        i=GPIO.input(14)
        if i:
            
            print("Motion Detected")
        else :
            print("Motion is not")
    
        
GPIO.add_event_detect(pirno, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(pirno, call)
while True:
    time.sleep(0.1)