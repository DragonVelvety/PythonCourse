# 1
# Create a list of numbers from 1 to 10. Use the pop() method 
# to remove the last element from the list and print the removed element. 
# Then print the updated list.

l=[1,2,3,4,5,6,7,8,9,10]
r=l.pop(-1)
print(r)
print(l)

# 2
# Again, create a list of numbers from 1 to 10. Use the pop() method to remove 
# the element at index 3 from the list and print the removed element. 
# Then print the updated list.
r=l.pop(3)
print(r)
print(l)

# 3
# Create a list of fruits. Use the remove() method to remove a specific fruit from the list. 
# Then print the updated list.

l=["Apples","Pears","Cherries","Grapes","Strawberries","Plums"]
l.remove("Grapes")
print(l)

# 4
# Again, create a list of fruits. Use the del keyword 
# to remove a slice of fruits from the list and print the updated list.

del l[1:3]
print(l)