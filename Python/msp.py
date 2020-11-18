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


#StartUP
#takes the user input / wipes the Screen / puts the input in to an array
answerInput = str(input("Please enter the word to be guessed: "))
print("\n" * 50)
for x in range (len(answerInput)):
  answerInputArray.append(answerInput[x])
  






while endCondition == 0:     #While the game has not been won or lost


    

    






  time.sleep(1)

  if endCondition == 1 :
    break

  
        


    


