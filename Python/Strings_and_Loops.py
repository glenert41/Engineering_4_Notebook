#Strings and Loops
#In this program, the user inputs a sentence, and then an it gets printed back letter for letter, with a minus as a space
#Graham Lenert

input = str(input("Enter your phrase: ")) #takes the input, and converts it to a string
input = input.replace(" ", "-")  #replaces all spaces with a - 

input_list = list(input)  #convertst the string to a list, in order to be printed with the correct syntax
input_list.append("-")  #adds a - to the end of the list 

print(*input_list, sep='\n') #prints the list, place by place, and returns each line


  
