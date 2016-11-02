#!/usr/bin/python

#This file is meant to demonstrate using functions. However since I've used functions before, I will attempt to use lamdas.

#add
add = lambda x,y: x+y

#subtract
subtract = lambda x,y: x-y

#multiply
multiply = lambda x,y: x*y

#divide
divide = lambda x,y: x/y

#while
while True:
	
	try:
		num1 = float(input("Enter a number: \n"))
		num2 = float(input("Enter a second number: \n"))
		function = str(input("Enter 'add', 'subtract', 'multiply', or 'divide': \n")).lower()
	except ValueError:
		print("Invalid entry... restarting \n")
		continue

	if function == "add":
		print(add(num1,num2))
	elif function == "subtract":
		print(subtract(num1,num2))
	elif function == "multiply":
		print(multiply(num1,num2))
	elif function == "divide":
		print(divide(num1,num2))
	else:
		print("not a valid operation, restarting...")