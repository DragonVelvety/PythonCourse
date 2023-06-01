# 1 Positional argument
# 2 Default argument
# 3 Keyword argument
# 4 Variable length positional arguments
# 5 variable length keyword arguments

# Function definition and call with two arguments for positional 
def linear_search(l,key):
	for value in l:
		if key==value:
			return True
	else:
		return False		

l=[100,200,300,400,500]
key=900

result=linear_search(l,key)
print(result)


# Function for generating a password based on the following requirements
# length of 8 characters
# 1 upper case letter
# 1 lower case letter
# 1 special character
# 5 digits

# ord
# chr

# print(ord("a"), ord("z")) # returns the ASCII value for lower case a and z (97-122)
# print(ord("A"), ord("Z")) # 65-90
# print(chr(97)) # returns the character represented by the specified ASCII value

import random
# setting length=8 as default - if nothing else is specified in the function call, 
# a pw with 8 characters will be generated
def gen_password(length=8):
	l=["@","#","?","!","$","&"]
	
	upper=chr(random.randint(65,90))
	lower=chr(random.randint(97,122))
	special=random.choice(l)
	digit=random.randint(10000,99999)
	password=upper+lower+special+str(digit)
	l=random.sample(password,length)
	password=("").join(l)
	return password

result=gen_password(5)
print(result)

# using the keywords username and password
# def validate(username,password):
# 	if username =="abc123" and password=="Abc@123":
# 		print("Valid password")
# 	else:
# 		print("Invalid password")	

# validate("abc123", "Abc@123")
# validate(password="Abc@123", username="abc123")

print(100,200, sep=",", end=" ")
print("Hi")

# l=[100,200,300,400]
# l.append(500)
# print(l)

def add_value(*args):
	l=[]
	for value in args:
		l.append(value)
	return l	

result=add_value(100,200,300,400,500)
print(result)
result=add_value(100,200)
print(result)
result=add_value(100,200,300,400,500,600,700,800)
print(result)

# for a form where the user can enter: name,email,contact number, date of birth

def get_details(**kwargs):
	print(kwargs)


get_details(name="ABC",email="abc@testinger.com",contact=1234567,dob="12-12-1999")
get_details(name="ABC",email="abc@testinger.com",dob="12-12-1999")
get_details(name="ABC",contact=1234567,dob="12-12-1999")
