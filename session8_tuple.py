# tuple
# immutable data type
# ordered data structure
# supports indexing and slicing
t=(10,20,20,20,30,30,40)
print(t, type(t))

print(t[-1])
print(t[:3])
print(t.index(20))
print(t.count(20))

l=[10,20,30,40,50]

for index,value in enumerate(l):
	print(index,value)
for t in enumerate(l):
	print(t)	

t=tuple(l)	
print(t)

t=("a","b","c",100)
l=list(t)
print(l)