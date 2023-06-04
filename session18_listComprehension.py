# List comprehension can be used if you have an iterable type of list 
# and want to perform the same operation on all elements of the list
# the output will be another list

# l = [100,200,300,400,500]
# l2 = [value*value for value in l]

# for value in l:
# 	l2.append(value*value)

# print(l2)	

# l = [10,20,25,30,35,60,65,70,85]
# l2 = [value for value in l if value%2 == 0]
# print(l2)

# l = ["abc","abcd","abcde","zzzzzz"]
# l2 = [len(value) for value in l]
# print(l2)

# if possible use list comprehension as it uses the append method implicitly 
# and it is good practice to use implicit calls rather than explicit calls 
# (because implicit method calls are faster)

# l2 = [(value1,value2) for value1 in range(1,10) for value2 in range(100,103)]
# print(l2)

# l = [[1,2,3],[4,5,6],[7,8,9]]
# l2 = [value2 for value in l for value2 in value]
# print(l2)

# for value in l:
# 	for value2 in value:
# 		l2.append(value2)

# print(l2)

# l = [100,105,110,115,120]

# l2 = ["Even" if value%2 == 0 else "Odd" for value in l]
# print(l2)

# d = {x:x**2 for x in range(1,11)}
# print(d)

d = {chr(x):x for x in range(97,123)}
print(d)

d2 = {value:key for key, value in d.items()}
print(d2)