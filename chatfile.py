#!/usr/bin/python3
import sys
import subprocess
import string

work = []

inputfile = sys.argv[1]
outputfile = str(sys.argv[2])

pre_text = str(sys.argv[3])
post_text = str(sys.argv[4])

with open(str(inputfile), 'r') as fi:
        for line in fi:
                work.append(line.strip())


new = []
for line in work:
        s = line
        translator = line.maketrans('', '', string.punctuation)
        line = line.translate(translator)
        line = pre_text + line + post_text
        new.append(line)
print(new)

ultimate = []
for line in work:
        feed = subprocess.run(["bash", "call", line], capture_output=True)
        x = feed.stdout.decode().strip('""').replace("\\n", "").strip('""').strip("''")
        ultimate.append(x)
        print(x)

print(ultimate)
with open(outputfile, "w") as F:
        F.writelines("%s\n" % item for item in ultimate)
