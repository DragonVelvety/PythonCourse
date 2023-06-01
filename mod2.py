import mod1

help(mod1)

l= [100,200,300,400,500]
key= 500

print(mod1.binary_search(l,key))

# If I import a module, python will execute the code in the file and create a __pycache__ directory

import math

# help(math)

#To create a package just create an empty directory named __init__.py. This will be considered 
# as a Python directory