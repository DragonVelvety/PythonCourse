# l = [100,200,300,400,500]
# i = iter(l)
# # print(i)

# print(next(i))
# print(next(i))

# for value in i:
# 	print(value)

import itertools

# l1 = [10,20,30,40,50]
# l2 = [100,200,300,400,500]
# l3 = [1000,2000,3000,4000,5000]

# i = itertools.chain(l1,l2,l3)
# # print(i)

# for value in itertools.islice(i,0,8):
# 	print(value)

# range(10,50)
# count = 0
# for value in itertools.count(10,5):
# 	if count > 20:
# 		break
# 	else:
# 		print(value)
# 	count+=1	

l = [1,2,3]

print(list(itertools.permutations(l,2)))

print(list(itertools.combinations(l,2)))

#print(next(i))

# for value in i:
# 	print(value)

# l = [10,20,30,40,50]
# count = 0
# for value in itertools.cycle(l):
# 	if count < 20:
# 		print(value)
# 	else:
# 		break	
# 	count+=1  


# l = [10,20,30,40,50]
# count = 0
# for value in itertools.repeat(l):
# 	if count < 20:
# 		print(value)
# 	else:
# 		break	
# 	count+=1  


#tee
# l = [10,20,30,40]
# i = iter(l)
# t = itertools.tee(i)
# print(t)

# for value in t[0]:
# 	print(value)

# for value in t[1]:
# 	print(value)	

# for value in i:
# 	print(value)
