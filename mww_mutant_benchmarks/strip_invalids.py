import os, os.path

with open('checkResult_copy.txt') as fp:  
	line = fp.readline()
	for cnt, line in enumerate(fp):
		if (line.startswith("C:\\Users")):
			currentFile = line
		elif (line.startswith("INVALID PROPERTIES")):
			if "jkind " in currentFile:
				path, file = currentFile.split("jkind ",1)
				file = file.strip()
				print(file)
				if (os.path.isfile(file)):
					os.remove(file)
		