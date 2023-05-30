# dict -- Hash table
# mutable data structure
# unordered data structure
# keys should be unique
# keys should be immutable -- int, float, str, tuple
d={"emp_id":101,"name":"Test Testinger","email":"test@testinger.de"}
print(d)

d["contact_no"]=1234567
print(d)

d["contact_no"]=7654321  # works both for adding and updating 
print(d)

print(d["email"])

# get
# setdefault
print(d.get("emp_id",-1))
print(d.get("age","Key does not exist"))
print(d.setdefault("emp_id"))

print(d.setdefault("age",50)) # setdefault will add the default element (and value) if it does not exist 
print(d)
print(d.keys())
print(d.values())
print(d.items())

for t in d.items():
	print(t)

for x in d:
	print(x)

for key in d:
	print(key,d[key])	


d={}
for value in range(1,11):
	d[value]=value*value
print(d)
