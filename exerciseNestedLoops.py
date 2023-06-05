import os

def read_input(dirName):
	for dirpath, dirnames, filenames in os.walk(dirName):
		for filename in filenames:
			path = os.path.join(dirpath, filename)
			ext = os.path.splitext(path)
			print("Extension:",ext[1])
			if ext[1] == ".html":
				print("Valid file", ext)
				#
			else:
				print("Invalid file")	

			 	

input = read_input("D:\My\Path\myDir")		