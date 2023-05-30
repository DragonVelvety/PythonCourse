l1=[1,2,3,4,5]
l2=[1,4,9,16,25]

d=dict(zip(l1,l2))
print(d)

l=[1,2,3,4,5]
d=dict.fromkeys(l,0)
print(d)

d1={1:1,2:4,3:9,4:16}
d2={5:25,6:36,7:49}
d1.update(d2)
print(d1)

d1={1:1,2:4,3:9,4:16}

# pop
# popitem
# clear
# del

r=d1.pop(2)
print(d1,r)

r=d1.popitem()
print(d1,r)
d1.clear()
print(d1)

# del d1