# Write a python program which iterates the integers between 1 and 50  
# For multiples of 3 print "Fizz", for multiples of 5 print "Buzz"
# For multiples of 3 and 5 print "FizzBuzz" 

number1 = 0

for value in range(1,51):
	resultFizz = number1%3
	resultBuzz = number1%5
	if resultFizz == 0 and resultBuzz == 0:
 		print("FizzBuzz")
	elif resultFizz == 0:		
 		print("Fizz")
	elif resultBuzz == 0:
		print("Buzz")
	else:
 		print(number1)
	number1 = number1+1
