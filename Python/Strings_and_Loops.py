#Strings and Loops
#In this program, the user inputs a sentence, and then an it gets printed back letter for letter, with a minus as a space
#Graham Lenert

string = str(input("Enter your phrase: ")) 
string = string.replace(" ", "-") 

string_list = list(string) 
#string_list.append("-") 

for x in string_list:
    print(x)

  
