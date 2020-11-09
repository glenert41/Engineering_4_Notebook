#This is a Python Calculator
#This is by Graham Lenert

inputNum1 = input("Press first number: ")
inputNum2 = input("Press second number: ")


def doMath(inputNum1,inputNum2,operator):
	if operator == 1:
		return int(inputNum1) + int(inputNum2)
	if operator == 2:
		return int(inputNum1) - int(inputNum2)
	if operator == 3:
		return int(inputNum1) * int(inputNum2)
	if operator == 4:
		Q = int(inputNum1) / int(inputNum2)
		RQ = round(Q,2)
		return RQ
	if operator == 5:
		return int(inputNum1) % int(inputNum2)

print("Sum:\t\t" + str(doMath(inputNum1,inputNum2,1)))
print("Difference:\t" + str(doMath(inputNum1,inputNum2,2)))
print("Prodcut:\t" + str(doMath(inputNum1,inputNum2,3)))
print("Quotient:\t" + str(doMath(inputNum1,inputNum2,4)))
print("Modulo:\t" + str(doMath(inputNum1,inputNum2,5)))
