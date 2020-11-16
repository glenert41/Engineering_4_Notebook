#Strings and Loops
#In this program, the user inputs a sentence, and then an it gets printed back letter for letter, with a minus as a space
#Graham Lenert

input = str(input("Enter your phrase: ")) 
input = input.replace(" ", "-") 

input_list = list(input) 
input_list.append("-") 

print(*input_list, sep='\n')


  
