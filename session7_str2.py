# help(str)
# print(dir(str))

# format

#number1 = 100
#number2 = 200

#print("Value of number2 is {1} and value of number1 is {0}".format(number1, number2))
#print("Value of number2 is {value2} and value of number1 is {value1}".format(value1=number1, value2=number2))

# s = "my python sample string"
# s1 = s.capitalize() # --> will only capitalize the first letter of the string
# print(s1)
# print(s1.isupper())
# print(s1.islower())
# s1 = s1.title()
# print("Title: ",s1.istitle())
#upper
#lower
#title
# s1 = s.upper()
# print(s1)
# print(s1.isupper())

# s1 = s.lower()
# print(s1) 
# print(s1.islower())

# split
# join

# s = "HTML,CSS,PYTHON,JAVA,DJANGO"
# l= s.split(",")
# print(l)

# s1 = (" ").join(l)
# print(s1)

# s2 = "abcdefg"
# s3 = "1234567"
# s4 = "Python Sample String abcdefg"

# # maketrans
# # translate

# table = str.maketrans(s2,s3)
# result = s4.translate(table)
# print(result)

# index
# find
# rfind

s = "HTML,CSS,PYTHON,JAVA,DJANGO,PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON"))

print(s.find("python"))
print(s.rfind("PYTHON"))

s = "*************This is my sample string**********************"
print(s)
s1 = s.strip("*")
s2 = s.lstrip("*")
s3 = s.rstrip("*")
print(s1)
print(s2)
print(s3)

s = "Python"
s1 = s.center(20,"*")
print(s1)
s2 = s.ljust(20,"*")
print(s2)
s3 = s.rjust(20,"*")
print(s3)

s4 = "html,css,python,html"
s5 = s4.replace("html","HTML5")
print(s5)