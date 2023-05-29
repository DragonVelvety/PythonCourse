# Write a python program to find those numbers 
# between 1500 and 2700 which are divisible by 5 and 7

# while loop for going through the numbers from 1500 to 2700
# conditional statements for checking if the number is divisible by 5 and 7  

start = 1500
end = 2700
divisibleNumbers = []

while start<=end:
	result = start%5
	if result == 0:
		print(start," is divisible by 5")
		result = start%7
		if result == 0:
			print(start, "is also divisible by 7")
			divisibleNumbers.append(start)
		else:
			print(start, "is not divisible by 7")			
		start=start+1			
	else:
		start=start+1
print(divisibleNumbers)