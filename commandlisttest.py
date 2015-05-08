import os

commandlist = open('commandlist.txt')

for line in commandlist.readlines():
	# line = line.rstrip('\n')
	print line
	# execute every line in the commandlist file inside the terminal
	os.system(line)