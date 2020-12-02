# Engineering_4_Notebook
My Engineering 4 Notebook - Get well soon Virgil van Dijk



## Introductory Raspberry Pi Assignments






### Hello Raspberry Pi

#### Description:

This is is Hello Raspberry Pi module. In this module, we connect the Raspberry Pi to our computer, and open the editor, in this case, Beagle Term. Then we had to make a basic program.

#### Code Link:

[Hello Raspberry Pi Code](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/hello_world.py)

#### Images:

<img src="Images/Screenshot%202020-10-14%20at%201.08.21%20PM%20(2).png" width="256*1.5">
                                                                               
<img src="Images/Screenshot%202020-10-14%20at%2012.56.37%20PM%20(2).png" width="256">


#### Reflection:

This module took 7 hours, although it was very easy. My issue was that when I open Beagle Term and hit enter, I do not get any response. The solution was to switch my TX and RX cables, as the label on them was incorrect.









### Get Your Pi Online

#### Description
This is the Get your Pi Online module. In this module, we had to connect our Pi to the internet, and then add the file from the Hello Raspberry Pi module to our Git Hub. We created folder on the Pi for our Engineering 4 Notebook Repo, and then we committed and pushed the file and folder to our Git Hub.

#### Code Link

N/A

#### Images

<img src="Images/Screenshot%202020-10-21%20at%201.15.39%20PM.png" width="256*2">
                                     
                             
#### Reflection
                      
This module took a bit of thinking and genuinely was difficult at times; the biggest take away for me was that you should not just type in what Dr. Shields has in the video, you should understand what each line, and really each word, does, as Beagle Term and Raspberry Pi can be unforgiving for learners like me. Also, when pushing to master, you may have to type main --- (git push origin master) or (git push origin main)

                                     
                                     
                                     
                                     
                                     
                                     
### Hello Python (Dice Roller)

#### Description
This is from the Hello Python module. In this module, we had to create a python file that would roll a die when enter was pressed, and when x was pressed, the program would quit.

#### Code Link

[Dicer Roller Code Link](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/dice_roller.py)

#### Images

<img src="Images/Screenshot%202020-10-29%20at%202.37.34%20PM.png" width="256*2">

#### Reflection

This module was definitely the most challenging to date. It really made me rely on the skills I developed in the prior assignments. I think, as mentioned in the previous module, that going back throught the assignment video and watching/noting what each line does really helped. The hard part for me wasn't writing the actual code, but rather manuvering through the Raspberry Pi interface; however I think I have the basics down now. On issue I had was how to detect if enter was pressed with an input, the way to solve this is by leaving the quotes blank in between. For example, instead of ("ENTER") just do (" ")





### Program 01 - Calculator

#### Description

In this module, we had to make a calculator in python. Essentially, we had to have the user input 2 numbers, then run those numbers through one function, and recieve the results of the 5 different operators (Addition, Subtraction, Multiplication, Division, Modulo)

#### Code Link

[Calculator Link](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/calculator.py)

#### Images

<img src="Images/Screenshot%202020-11-09%20at%2012.56.04%20PM.png" width="256*2">

#### Reflection

This module was very fun for me. At first, I went through and didn't use a function (Which cost me a class period of work because I didn't fully read the directions. Life lesson 1 -- read the directions.) Anyways, my biggest takeaway from this module was really reafirriming how to use functions in python with parameters. Essentially, in the function definition, you have to declare that this function will need parameters (values) in order to run, and then it will use those values you give the function when you call it later on to give you the result.




### Program 02 - Quadratic Solver

#### Description

In this module, we had to make a quadratic solver, meaning the user would give their a,b, & c values for standard form of a quadratic, and then the program would produce the roots, and if there were no roots, then the program would produce that there were no roots.

#### Code Link

[Quadratic Solver Link](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/quadratic_solver)

#### Images

<img src="Images/Screenshot%202020-11-13%20at%205.27.03%20PM.png" width="256*2">

#### Reflection

This module was pretty straight forward. It was cool to see the power that arrays had, and I definitely plan to use them in the future. The hardest part for me though was getting used to arrays. You can print the values of the array, and even print the array, but there will still be brackets around the values. In this case, you have to place a string of the value of each position in the array. Something that I thought was cool though is that you are able to mix numbers and letters in an array, which lets you store different types of values in one array. Also, if you want to add a value to an array, you have to add append it (ARRAYNAME.append("value")).



### Program 03 - Strings and Loops (String Splitter)

#### Description

In this module, we had to make a program that would take an input sentence, and then print the input out letter by letter, and with a - sign instead of a space.

#### Code Link

[String Splitter](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/Strings_and_Loops.py)

#### Images

<img src="Images/Screenshot%202020-11-16%20at%209.37.50%20PM.png" width="256*2">

#### Reflection

There were plenty of different ways to do this module. I began with roughly 10 lines of code. Then broke it down in to smaller and more concise lines, until I was able to have around 5 remain. I think my favorite way of printing items in a list is by doing this doing  print(*LIST_NAME, sep='\n').* This was seemingly the most efficient way to print each element on its own line. You could also do something with a for loop, like as follows .... for X in LISTNAME: print(x) ... This works well when you have other operations to do in the for loop. I expect to be using the later in the upcoming module. Also, in order to replace an item in the list, just use the replace() function. For example ... stringName = stringName.replace("w", "t")  ... This replaces all w's in the list with t's.
 
 
 
 
 ### Program 04 - Man Shaped Piñata
 
 
 #### Description
 
In this assignment, we had to recreate the classic game Hangman; or as we're going to call it, Man-Shaped Piñata. The game is simple, one player inputs a word, and another player has to guess the other player's word, by guessing lettter by letter. If the 2nd player guesses an incorrect letter, the program will draw a part of Franklin the Turtle without his shell; and you don't want to see Franklin the Turtle without his shell now don't you...?
 
 #### Code Link
 
 [Man Shaped Piñata](https://github.com/glenert41/Engineering_4_Notebook/blob/main/Python/msp.py)
 
 #### Images
 
 <img src="Images/Screenshot%202020-12-02%20at%2012.22.50%20PM.png" width="256*2">
 
 <img src="Images/Screenshot%202020-12-02%20at%2012.23.34%20PM.png" width="256*2">
 
 #### Reflection
 
 This assignment was the first assignment this year to really make me think about the process of the assignment. At first, it was really daunting to create the game, but I ended up breaking the assignment down in to 3 different phases (1: Get the user input, create an array with those letters, and then create an array with the same amount of underscores as the length of the input 2: Get the program fully functioning, without the MSP image. 3: Add to the MSP Image after every missed letter. The most difficult part for me was testing whether or not the letter was in the list/array. In order to overcome this, it is acutally quite simple, you can just use the "in" or "not in" feature in python. (Something like this....      if ELEMENT in LIST:   or if ELEMENT not in LIST)
 
 
 
 
 
 
 
 
 
 
 



