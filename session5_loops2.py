# break
# continue
# enumerate

#for value in range(10):
#	print(value)

l = [10,20,30,40,50,60]
key = 400

for index,value in enumerate(l):
	#print(index,value)
	if value == key:
		print("Element found at index",index)
		break
	else:
		continue
		#pass
		print("Statement after continue") #--> unreachable for continue as program will skip directly to else
else:
	print("Element not found")	
print("Statement after the for loop")			