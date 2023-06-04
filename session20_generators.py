# generator functions are a special type of function that can retain the state of the function
# and will return one value at a time

# def printVal(l):
# 	for value in l:
# 		yield(value)

# l = [10,20,30,40,50,60]

# g = printVal(l)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def fibo():
# 	firstNum = 0
# 	secondNum = 1
# 	yield secondNum
# 	while(True):
# 		nextVal = firstNum + secondNum
# 		# If a yield statement is used in a function, the function is called a sa generator function
# 		yield nextVal
# 		firstNum, secondNum = secondNum,nextVal
# If a generator function is called, the function is not executed but the generator object is returned
# g = fibo()
# print(g)

# When next is used,  
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for value in range(10):
# 	print(next(g))

# for value in range(20):
# 	print(next(g))	

l = [10,20,30,40,50,60]
l2 = (value*value for value in l)
# print(l2)

print(next(l2))
print(next(l2))
print(next(l2))

# generators reduce the memory consumption of your code