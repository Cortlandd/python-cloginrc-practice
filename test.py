import os
# import sys

switchlist = open('switchlist.txt')

commandlist = open('commandlist.txt')

for lines in switchlist.readlines():

	lines = lines.rstrip('\n')

	if (len(lines) == 0):

		continue

	elif (line == '#EOF'):

		break

	elif (line[0] != '#'):
	
	
# os.system('ifconfig')