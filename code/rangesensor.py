import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 


def calculate_distance():
	GPIO.setmode(GPIO.BCM)
	TRIG = 18
	ECHO = 23 

	print("Using RPI ZERO and HC SR04 for distace measurement...in porogres")

	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	GPIO.output(TRIG, False)
	print("Waiting for senosr to settle down")
	time.sleep(2)

	#sending the pulse 
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	#record just after sending the pulse what was the last time the echo pin was lOW
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	#record the time when echo pin became high 
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()  

	pulse_duration = pulse_end - pulse_start
	print (pulse_duration)

	distance = pulse_duration * 17150
	distance = round(distance, 2)
	print ("Distance:",distance,"cm")

	GPIO.cleanup()
	return distance
