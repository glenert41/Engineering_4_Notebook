#MSP and/or Hangman game
#Graham Lenert
# This program plays the hangman game


import time
import os




endCondition = 0  

#creates the arrays and lists (no values in them)
answerInputArray = []
wordBoardArray = [] # answer list that you can see
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

  #asks for your guess and makes it lower case
  guessLetter = str(input("Guess a letter: ").lower())

  




  
  # If guess letter has already been guessed
  if guessLetter in guessedList:
      print("\n")
      print("Already guessed")
      print("\n")
      continue #go back to the while loop start

  # if guess letter has not already been guessed; and is right
  if guessLetter not in guessedList:
    guessedList.append(guessLetter)  #add the letter guessed to list of already guessed letters
    
    # go through each letter in the answer and check if it matches thre guess
    for x in range(len(answerInputArray)): 

        # if the letter is the word, add guess to answer
        if str(answerInputArray[x]) == str(guessLetter):

            
            #adds correct guess to word board 
            wordBoardArray[x] = guessLetter
            wordBoardList = list(wordBoardArray)

            

  # If guessed letter is wrong
  if guessLetter not in list(answerInputArray):
      #print("added to hangman")
      
      #take away a guess
      guessAttempts = guessAttempts - 1

      #draws the hangman
      draw(int(guessAttempts))
      
      
  print("\n") #returns a little
  print(*wordBoardList, sep=' ') #print the list of letters
  print("Guess Attempts Remaining: " + str(guessAttempts)) #primt how many guesses you have left
  print("Letters Guessed: " + str(guessedList)) #print what lettersd you have guessed
  print("\n" * 5) #returns a lot


  #if the letters you've guessed match the answer
  if wordBoardArray == answerInputArray:
      WC = 1
      break #quit the while loop

  # if you have 0 remaining guesses
  if guessAttempts == 0:
      WC = -1
      break #quit the while loop
      
  

  time.sleep(1)

  

if WC == 1: #prints win or lose
  print("You Win")
elif WC == -1:
  print(" You Lose")

    


