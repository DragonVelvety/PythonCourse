# factorial(5) = 5* fact(4)
# 						 4 * fact(3)
#							 3 * fact(2)
# ...
# import math

# def factorial(num):
# 	if num == 1:
# 		return 1
# 	else:
# 		return num * factorial(num-1)	

# number1 = 5
# result=math.factorial(number1)
# print(result) 		

# factorial(5)    5  * 24 = 120
# 					 4 * 6 = 24
# 					     3* 2 = 6
# 					     	2 * 1 = 2
# 					     			1		

l=[100,200,300,400,500,600,700,800,900]
key=100

def binary_search(l,key):

	if len(l) == 0:
		return False
	else:		
		mid = len(l) // 2
		if l[mid] == key:
			return True
		
		elif key < l[mid]:
		 	return binary_search(l[:mid],key)	
		else:
		 	return binary_search(l[mid+1:],key)		

result = binary_search(l,key)
print(result)

# mid = 9 / 2 = 4 = 500 == 700 True
# [600,700,800,900]
# mid = 4 / 2 = 2 = 800 == 700
# [600,700]
# mid = 2/2=1=700 == 700 True