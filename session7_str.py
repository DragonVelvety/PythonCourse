# Strings
# Strings are immutable
# String is an ordered data structure --> it suports indexing and slicing
# Indexing works from left to right (positive numbers) and from right to left (negative numbers)

# Indexing
s = "My Python sample string"
print(s[5])
print(s[-1])

# Slicing
print(s[9:23])
print(s[9:])
print(s[ :23])

#Stride
print(s[::-2])

for value in s[::2]:
	print(value)	
