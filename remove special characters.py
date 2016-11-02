#!/usr/bin/python

#this is meant to practice removing characters from a string
initial = input("enter a string, special characters will be removed ")
specialcharacters = '!@#$%^&*()_-=+[]{}/\\'

def removespecialcharacters(string):
	print("you entered: ",string)
	for c in string:
		for s in specialcharacters:
			if c == s:
				index = string.find(c)
				string = string[:index] + string[index+1:]
	print(string)

removespecialcharacters(initial)