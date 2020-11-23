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
answerInput = str(input("Please enter the word to be guessed: "))
print("\n" * 50)
for x in range (len(answerInput)):
  answerInputArray.append(answerInput[x])
  wordBoardArray.append("_ ")

wordBoardList = list(wordBoardArray)






while endCondition == 0:     #While the game has not been won or lost

  guessLetter = str(input("Guess a letter: "))

  for x in range(len(answerInputArray)):

      # if the letter is the word
      if str(answerInputArray[x]) == str(guessLetter):
          wordBoardArray[x] = guessLetter
          wordBoardList = list(wordBoardArray)


  if guessLetter not in list(answerInputArray):
      print("Time to start hangman")




  print(*wordBoardList, sep=' ')
  






  if wordBoardArray == answerInputArray:
      endCondition = 1

  if endCondition == 1 :
    break
  

  time.sleep(1)

  
        
print("You win")

    


