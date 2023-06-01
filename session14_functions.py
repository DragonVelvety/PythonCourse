# Main advantages of using functions
# 1 Code reuse
# 2 Mudularity

#s="Python, HTML,CSS"
#print(s.index("HTML"))


# function definition - function definitions can not be executed without a function call
def value_reverse(value):
	if type(value)==list or type(value) ==str:
		reverse=value[::-1]
	else:
		tmp=str(value)	
		reverse=tmp[::-1]
	return(reverse)

# function call
s="Python"
result=value_reverse(s)
print(result)

# l=[10,20,30,40]
# l.append(50)
# print(l)

l=[100,200,300,400]
result=value_reverse(l)
print(result)

number1=100
result=value_reverse(number1)
print(result)