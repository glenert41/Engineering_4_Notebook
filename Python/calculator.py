#This is a Python Calculator
#This is by Graham Lenert

inputNum1 = input("Press first number: ")
inputNum2 = input("Press second number: ")


def doMath(inputNum1,inputNum2,operator):
	if operator == 1:
		return int(inputNum1) + int(inputNum2)
	if operator == 2:
		return int(inputNum1) - int(inputNum2)


print("Sum:\t\t" + str(doMath(inputNum1,inputNum2,1)))
print("Difference:\t\t" + str(doMath(inputNum1,inputNum2,2)))
