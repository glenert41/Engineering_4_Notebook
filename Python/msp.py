#MSP and/or Hangman game


import time
import os




endCondition = 0  

#creates the arrays and lists (no values in them)
answerInputArray = []
wordBoardArray = []
wordBoardList = list(wordBoardArray)


#StartUP
#takes the user input in lower case / wipes the Screen / puts the input in to an array
answerInput = str(input("Please enter the word to be guessed: ").lower()) 

print("\n" * 50) #clears the screen

for x in range (len(answerInput)):
  answerInputArray.append(answerInput[x])
  wordBoardArray.append("_ ")
  #creates the array where you answer with the correct amount of underscores




guessedList = []
guessAttempts = 5 #5 guess attempts to start
WC = 0 #win condition variable


#function that draws Franklin
def draw(n):  
    print("\n" * 2) #returns a few lines for clarity
    f = open("banner.txt", "r") #opens the Franklin file

    #prints a cwrtain amount of lines based on guesses Remaining
    for x in range(0, (5-n) * 8 + 1):
        print(f.readline(), end="")





while endCondition == 0:     #While the game has not been won or lost

  guessLetter = str(input("Guess a letter: ").lower())

  




  
  # If guess letter has already been guessed
  if guessLetter in guessedList:
      print("\n")
      print("Already guessed")
      print("\n")
      continue

  # if guess letter has not already been guessed; and is right
  if guessLetter not in guessedList:
    guessedList.append(guessLetter)
    

    for x in range(len(answerInputArray)):

        # if the letter is the word
        if str(answerInputArray[x]) == str(guessLetter):

            

            wordBoardArray[x] = guessLetter
            wordBoardList = list(wordBoardArray)

            

  # If guessed letter is wrong
  if guessLetter not in list(answerInputArray):
      print("added to hangman")
      

      
      guessAttempts = guessAttempts - 1

      draw(int(guessAttempts))
      
      
  print("\n")
  print(*wordBoardList, sep=' ')
  print("Guess Attempts Remaining: " + str(guessAttempts))
  print("Letters Guessed: " + str(guessedList))
  print("\n" * 5)



  if wordBoardArray == answerInputArray:
      WC = 1
      break

  if guessAttempts == 0:
      WC = -1
      break
      
  

  time.sleep(1)

  

if WC == 1:
  print("You Win")
elif WC == -1:
  print(" You Lose")

    


