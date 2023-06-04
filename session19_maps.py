# map
# filter
# lambda
## map, filter and lambda functions are much faster than list comprehension and normal functions

# def sqr(number1):
# 	return number1**2

# l = [10,20,30,40,50,60]

# result = list(map(sqr,l))
# print(result)

# for value in result:
# 	print(value)

# map
# def add(number1,number2):
# 	return number1+number2

# # for a map object, the output will alwas have the same length as the input
# l = [100,200,300,400,500]
# l2 = [10,20,30,40,50]

# result = list(map(add,l,l2))
# print(result)

# filter
# def check_num(number1):
# 	if number1%2 == 0:
# 		return True
# 	else:
# 		return False
# l = [100,115,120,125,130,140]

# result = list(filter(check_num,l))
# #result = list(map(check_num,l))
# print(result)

# lambda
# use lambda for small and uncomplicated functions 
# l = [10,20,30,40,50,60]
# result = list(map(lambda number1:number1**2,l))
# print(result)

# def check_num(number1):
# 	if number1%2 == 0:
# 		return True
#  	else:
# 		return False
l = [100,115,120,125,130,140]

result = list(filter(lambda number1:number1%2==0,l))
#result = list(map(check_num,l))
print(result)

d = {1:50,2:40,3:30,4:20,5:10}
l = dict(sorted(d.items(),key=lambda x:x[1]))
print(l)