# Automatic Dice Roller
# Written by Graham Lenert

from random import randint
import sys 
import time

print ("Automatic Dice Roller") 	#Show the Program is running


while True:			#This while loop continues to run, allowing for multiple inputs 
	time.sleep(1)		#Just a delay to not overwhelm the Pi
	RollPrompt = input("Press Enter to Roll and x to quit: ")	#asks user for input, stores as variable
	
	if RollPrompt == (""):
		print(randint(1,6))	#if the input is enter (empty), then choose random number 1-6
	if RollPrompt == ("x"): 	
                sys.exit()		#if the input is x, quit the program
		



	
		
