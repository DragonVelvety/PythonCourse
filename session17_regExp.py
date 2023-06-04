# Regular expressions
import re

# . any character except new line
# [a-zA-Z] - character class - a or b or c ... or A or B ...
# [0-9] - digit class - 0 or 1 0r 2 ...
# + at least 1 --> [a-z]+ 
# * 0 or more [a-z]* 

# ^ - match at start of string
# $ - match at end of string
# ? - optional 

# [a-z]{4} four characters 
# [a-z]{2,4} at least 2 at most four characters 

# s = "ABCDE1234A"
# r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")

# l = re.findall(r,s)
# print(l)

s = "+91 8123456789" 
r = re.compile("(?:\+91\s)?([6-9][0-9]{9})")
#r = re.compile("(+91)")
#l = re.findall(r,s)
m = re.search(r,s)
# print(l)

if m:
	print(m.group(1))
else:
	print("Pattern not found")	

# s = "12-05-2023"
# r = re.compile("^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
# # r = re.compile("^[0-3][0-9]-[0-1][0-2]-[0-2][0-9]{3}$")
# # l = re.findall(r,s)
# # print(l)

# m = re.search(r,s)
# if m:
# 	print(m.group("year"))
# else:
# 	print("Pattern not found")	

# [0-9] \d - digit class
# [^0-9] \D - anything but digits

# [a-zA-Z0-9] \w
# [a-zA-Z0-9] \W anything but alphanumeric values
# space \s
# anything other than space \S 
