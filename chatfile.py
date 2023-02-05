#!/usr/bin/python3
import sys
import subprocess
import string
import os
import time

work = []
inputfile = sys.argv[1]
outputfile = str(sys.argv[2])
pretext = str(sys.argv[3])
posttext = str(sys.argv[4])

with open(str(inputfile), 'r') as fi:
	for line in fi:
		work.append(line.strip())

def writer(newline):
	with open(outputfile, "a") as F:
		F.write("{newline}\n")

def double_check(new, dicto):
	if new in dicto.keys():
		dicto[new] += 1
	else:
		dicto[new] = 1

def final_check(dicto):
	death = False
	for entry in list(dicto.keys()):
		if dicto[entry] > 1:
			print(entry)
			death = str(input("Should I exclude this entry? y/n ")).lower()
			if death == "y" or death == "yes":
				del dicto[entry]
			elif death == "n" or death == "no":
				print("Entry will be kept in the output file.")
	with open(outputfile, "w") as F:
		F.writelines("%s\n\n" % item for item in dicto.keys())

new = []
for line in work:
	translator = line.maketrans('', '', string.punctuation)
	line = line.translate(translator)
	line = pretext + " " + line + " " + posttext
	new.append(line)

ultimate = []
checkmate = {}

for line in new:
	feed = subprocess.run(["bash", "call", line], capture_output=True)
	x = feed.stdout.decode().strip('""').replace("\\n", "").strip('""').strip("''")
	ultimate.append(x)
	double_check(x, checkmate)
	writer(x)

final_check(checkmate)	
print(ultimate)
