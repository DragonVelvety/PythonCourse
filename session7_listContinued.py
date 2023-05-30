# updating
l=[10,20,30,40,50]
l[2]=300
print(l)

# pop -- removes the last element from the list, returns the removed element - here r
# remove
# clear
# del
r=l.pop(1)
print(l,r)

l=[10,20,20,30,30,20,40,50]
l.remove(20)
print(l)
l.remove(20)
print(l)
l.clear()
print(l)
del l

l=[50,40,30,30,20,30,10]
#l.sort()
#print(l[::-1])
l.reverse()
print(l)

l3=sorted(l) # The sorted function can sort any data type
print(l3) 

# index
print(l.index(30)) # The index function only returns the first occurrence of the specified value

# count
print(l.count(30))

l=[10,20,20,30,40]
l2=[100,200,300]
print(l+l2) # concatenates both lists for the output. The original lists are not modified

l=[0.9]
print(l*10) # prints the same element 10 times