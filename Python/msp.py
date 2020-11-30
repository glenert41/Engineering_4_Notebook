#MSP and/or Hangman game

# Steps
# 1: Asks player for the word 
# 2: Clear the Screen
# 3: Loop
    #: print the wordBoard
    # if wordBoard is still open & Hangman is not complete:
      # Ask Player for Letter
          # if Letter is in word
            #update wordBoard
              
          # if Letter is NOT in word  
              # Draw next hangman piece  
    # if wordBoard is closed:
        #Game Win!


import time



endCondition = 0  

answerInputArray = []
wordBoardArray = []


#StartUP
#takes the user input / wipes the Screen / puts the input in to an array
answerInput = str(input("Please enter the word to be guessed: ").lower())
print("\n" * 50)
for x in range (len(answerInput)):
  answerInputArray.append(answerInput[x])
  wordBoardArray.append("_ ")

wordBoardList = list(wordBoardArray)

guessedList = []
guessAttempts = 5
WC = 0




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
  print("Win")
elif WC == -1:
  print("Lose")

    


