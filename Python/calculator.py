#This is a Python Calculator
#This is by Graham Lenert

#Asks user for their numbers, then stores the value
inputNum1 = input("Press first number: ") 
inputNum2 = input("Press second number: ")


def doMath(inputNum1,inputNum2,operator):
	#Do Math Function, takes the 2 user numbers, and decides which operator to use, and returns the value
	if operator == 1: #sum
		return int(inputNum1) + int(inputNum2)
	if operator == 2: #difference
		return int(inputNum1) - int(inputNum2)
	if operator == 3: #product
		return int(inputNum1) * int(inputNum2)
	if operator == 4: #quotient
		Q = int(inputNum1) / int(inputNum2) #finds quotient
		RQ = round(Q,2) #rounds quotient to 2 places
		return RQ
	if operator == 5: #modulus
		return int(inputNum1) % int(inputNum2)

#prints the operator name, and the doMath result of that operator using the two user numbers
print("Sum:\t\t" + str(doMath(inputNum1,inputNum2,1)))
print("Difference:\t" + str(doMath(inputNum1,inputNum2,2)))
print("Prodcut:\t" + str(doMath(inputNum1,inputNum2,3)))
print("Quotient:\t" + str(doMath(inputNum1,inputNum2,4)))
print("Modulo:\t\t" + str(doMath(inputNum1,inputNum2,5)))
