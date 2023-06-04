# Python provides different modes for opening a file
# r  --> read
# r+ --> read and write (append new content to existing content)
# w  --> write
# w+ --> overwrite existing content
# fp = open("inputText.txt","r+")
# content = fp.read()
# print(content)
# fp.write("\n\nSample line added later")

# content = fp.read()
# print(content)

# content = fp.read(30)
# print(content)

# readlines
# readline

# content = fp.readlines()
# print(content[:5])

# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)

# for x in fp:
# 	print(x)

# tell --> shows current file pointer position

# fp.write("Hello, write this new string.")
# print(fp.tell())
# content = fp.read()
# print(fp.tell())
# print(content)

# seek(offset,position) --> changes the current file pointer position
# offset --> number of characters
# position -->  0 --> start of the file
#				1 --> current position
#				2 --> end of the file	

# seek(15,0) --> change the file pointer position by 15 characters from the start of the file

# fp.write("Hello, this is my third string.")
# print(fp.tell())
# fp.seek(0,0)
# print(fp.tell())
# content = fp.read()
# print(fp.tell())
# print(content)

# a 
# a+

# r,r+,w,w+ pf is at the start
# a and a+ the fp is at the end

fp = open("inputText.txt","a+")
fp.write("\n\nNew text")

# r --> fp is at the start, file should already exist, read only
# r+--> fp is at the start, file should already exist, read and write
# w --> fp is at the start, creates a new file if it does not exist, write only
# w+--> fp is at the start, creates a new file if it does not exist, read and write
# a --> fp is at the end, creates a new file if it does not exist, write at the end only
# a+--> fp is at the end, creates a new file if it does not exist, read and write