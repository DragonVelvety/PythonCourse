# sets
# sets are mutable data structures
# All elements of a set should e unique
# Only immutable elements are supported -- int, float, tuple, str
# Sets are unordered data structures

s={10,20,30,40}
print(s,type(s))

s={100,200,300,400}
s.add(500)
print(s)

s1={10,20,30,40,50,60}
s2={40,50,60,70,80,90}

s3=s1.union(s2) # will merge the elements of s1 and s2 in the new set s3 
print(s3)

s3=s1.intersection(s2) # all elements which are in s1 and s2
print(s3)

s3=s1.difference(s2) # all elements of s1 which are not in s2
print(s3)

s3=s2.difference(s1) # all elements of s2 which are not in s1
print(s3)

s3=s1.symmetric_difference(s2) # all elements of s1 and all elements of s2 except common elements
print(s3)

print(s1)
s1.update(s2)
print(s1)

#s1.intersection_update(s2)
#print(s1)

#s1.difference_update(s2)
#print(s1)
#s1.symmetric_difference_update(s2)
#print(s1)

s1={100,200,300,400,500}
s2={100,200,300}

print(s2.issubset(s1))
print(s1.issuperset(s2))

l=[100,200,300,400]
s=set(l)
print(s)

l1=[100,200,300,400,500]
l2=[50,100.150,200,250,500,45,35,20,10]

s1=set(l1)
s2=set(l2)
s3=s1.union(s2)
print(s3)
l3=sorted(s3)
print(l3)

# l3=list(s3)
# l3.sort()
# print(l3)

# pop
# remove
# discard
# clear
# del

s={100,200,300,400,500,600}
# r=s.pop()
# print(s,r)

# s.remove(200)
# print(s)

s.discard(100)
print(s)

s.clear()
print(s)


