#Strings and Loops
#In this program, the user inputs a sentence, and then an it gets printed back letter for letter, with a minus as a space
#Graham Lenert

inputSentence = input("Enter your phrase: ")


splitArray = inputSentence.split()

for i in range (len(splitArray)):
  #this is new
