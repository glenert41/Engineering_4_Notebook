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






while endCondition == 0:     #While the game has not been won or lost

  guessLetter = str(input("Guess a letter: ").lower())

  
  guessedList = []
  guessAttempts = 0

  if guessLetter in guessedList:
      print("Already guessed")

  if guessLetter not in guessedList:

   for x in range(len(answerInputArray)):

        # if the letter is the word
        if str(answerInputArray[x]) == str(guessLetter):

            

            wordBoardArray[x] = guessLetter
            wordBoardList = list(wordBoardArray)

            
            guessedList.insert(guessAttempts, guessedList)
            guessAttempts = guessAttempts + 1



  # If guessed letter is not part of the word
  if guessLetter not in list(answerInputArray):

      guessedList.insert(guessAttempts,guessedList)
      guessAttempts = guessAttempts + 1
      
      print("Added to Hangman")





  print(*wordBoardList, sep=' ')
  print(guessAttempts)
  print(guessedList)
  






  if wordBoardArray == answerInputArray:
      break
  

  time.sleep(1)

  
        
print("You win")

    


