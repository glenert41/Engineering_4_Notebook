import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # sets weird warnings to false
leds = [38] # list with LED pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT) # sets board pins 38 and 40 to output

for i in range(0, 3): # blinks the LED's 10 times
	GPIO.output(38, 1)
	time.sleep(0.5)
	GPIO.output(38, 0)
	time.sleep(0.5)
	print("hi")
