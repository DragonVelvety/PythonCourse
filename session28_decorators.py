# A decorator is a special type of function that takes 
# a function as a parameter and returns another function
def deco(func):
	def new_func(value1,value2):
		if type(value1)==type(value2):
			return func(value1,value2)
		else:
			return func(str(value1),str(value2))	
	return new_func

@deco
def concat(value1,value2):
	return value1 + value2

result = concat(10,10)
print(result)

result = concat("Python","String")
print(result)