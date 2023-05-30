# lists
# Lists are mutable - add update and delete
# Lists support indexing and slicing
# heterogenous datatype 
l = [10,20,30,40,"Python","Java",[100,200,300]]
print(l, type(l))

# indexing and slicing
print(l[-1][1]) # this will return 200 as we are referencing the second entry of the list element list

print(l[1:3])
print(l[::-1])

l = [100,200,300,400,500]

for value in l[::2]:
	print(value)

# append
print(id(l))
l.append(600)
print(id(l))
print(l)

# extend
l.extend([700,800,900])
# extend will add multiple individual list elements to a list [100, 200, 300, 400, 500, 600, 700, 800, 900]
# append will add a specified list as one list element to the list [100, 200, 300, 400, 500, 600, [700, 800, 900]]
# extend will iterate over string characters and add them separately [100, 200, 300, 400, 500, 600, 700, 800, 900, 'P', 'y', 't', 'h', 'o', 'n']
l.extend("Python")
print(l)

# insert
l.insert(1,1000)
print(l)

l=[10,20,30]
l2=l
l2=l.copy()
l.append(40)
print(id(l),id(l2))
print(l,l2)		