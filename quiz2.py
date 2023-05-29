# Write a python program to count the number of even and odd numbers  
# between 1 and 9
# Expected output: 
# Number of even numbers: 5
# Number of odd numbers: 4 

number1 = 0
evenNumbers = 0
oddNumbers = 0

for value in range(1,101):
	result = number1%2
	if result == 0:
 		print("The specified number is even")
 		number1 = number1+1
 		evenNumbers = evenNumbers+1
	else:
 		print("The specified number is odd")
 		number1 = number1+1
 		oddNumbers = oddNumbers+1
print("Number of even numbers: ",evenNumbers)
print("Number of odd numbers: ", oddNumbers)