# Automatic Dice Roller
# Written by Graham Lenert

from random import randint
import sys 
import time

print ("Automatic Dice Roller")


while True:
	time.sleep(1)
	RollPrompt = input("Press Enter to Roll and x to quit: ")
	
	if RollPrompt == (""):
		print(randint(1,6))
	if RollPrompt == ("x"): 
                sys.exit()	
		



	
		
