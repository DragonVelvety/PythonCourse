l=[100,200,300,400,500]
print(sum(l))
print(max(l))
print(min(l))

number=25.555
print(round(number,2))

# print(dir(__builtins__))
# help(__builtins__)

import math

l=[0.1*10]
# print(sum(l))
print(math.fsum(l))

number=25.5559
print(math.floor(number), math.ceil(number))
print(math.sqrt(math.floor(number)))
print(math.factorial(5))

number1=46.56789
print(math.modf(number1))

d,i=math.modf(number1)
print(i,d)

print(math.pow(5,3))

print(math.log(10,2))
print(math.log10(2))
print(math.log2(10))

print(math.sin(math.radians(20)))
print(math.cos(math.radians(20)))
print(math.tan(math.radians(20)))

# help(math)
# print(dir(math))

import random

# print(random.random()) # generate a random number 

l=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(l))

print(random.randint(1,3)) # end number included
print(random.randrange(1,3)) # end number not included 

print(random.uniform(10,20))