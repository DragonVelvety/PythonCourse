# Loops in python
# 1 For loops
# 2 While loops
# Iterable datatypes: str, list, tuple, dict, set
 
# for [variableName] in [iterableDataType]:
#	statements

l = [10,20,30,40,50]

sum = 0

for value in l:
	sum = sum + value
	#print(sum)

print(sum)

#range(5) # 1,2,3,4
#range(10,100) # 10 bis 99
#range(10,100,5) # 10,15,20 ... 95

#for value in range(10,101,5):
#	print(value)

sum = 0
for value in range(1,21):
	sum = sum + value
	print(sum)
print(sum)	
