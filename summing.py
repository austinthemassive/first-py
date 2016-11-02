#!/usr/bin/python

#we want to take a user input and sum all numbers from 1 to that input

#take the input
retry = False
number = 0
condition = True
while condition == True:
	#function to handle non-numeric situations
	def numerictest(a):
		try:
			integer = int(a)
			retry = False
			return True
		except ValueError as inst:
			print(type(inst))
			print(inst)
			retry = True
			return False

	#function to handle non positive or non-integer
	def positiveintegertest(a):
		if abs(int(a)) != a:
			retry = True
			return False
		else:
			retry = False
			return True	

	number = 0
	if retry == False:
		number = int(input("Enter a positive integer "))
	elif retry == True:
		number = int(input("That is not a positive integer. Please enter a positive integer "))
		print(str(number))

	if (numerictest(number) == True and positiveintegertest(number) == True):	
		condition = False
	else:
		retry = True


#sum the value and all integers less than the value
total = 0
for x in range(number+1):
	total += x
print("The sum of all positive integers equal to and less than %i is %i" %(number,total))