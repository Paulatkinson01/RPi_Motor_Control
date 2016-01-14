import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

def forward():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(24,GPIO.HIGH)
	GPIO.output(25,GPIO.LOW)
	print ("FORWARD")

def stop():
	GPIO.output(18,GPIO.LOW)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	print ("STOP")

def left():
	GPIO.output(18,GPIO.LOW)
	GPIO.output(23,GPIO.HIGH)
	GPIO.output(24,GPIO.HIGH)
	GPIO.output(25,GPIO.LOW)
	print ("LEFT")
	
def right():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.output(25,GPIO.HIGH)
	print ("RIGHT")
	
while True:
	right()
	time.sleep(2)
	
	stop()
	time.sleep(2)

	forward()
	time.sleep(2)
	
	stop()
