import re
strings = []
numcharsPart1 = 0
numcharsPart2 = 0

def ascii(x):
	return chr(int(x.group(0)[2:], 16))

with open("input.txt") as f:
	content = f.read().splitlines()
	for line in content:
		strip = line.strip()
		edit = strip
		edit = edit[1:-1]
		edit = re.sub(r"\\x[a-f0-9]{2}", ascii, edit)
		edit = edit.replace("\\\"", "\"")
		edit = edit.replace("\\\\", "\\")
		#strings.append(edit)
		#print strip + " : " + str(len(strip)) + " " + edit + " : " + str(len(edit))
		numcharsPart1 += (len(strip) - len(edit))
		#print numcharsPart1
with open("input.txt") as f:
	for line in content:
		strip = line.strip()
		edit = strip
		edit = edit.replace("\\", "\\\\")
		edit = edit.replace("\"", "\\\"")
		edit = "\"" + edit + "\""
		numcharsPart2 += len(edit) - len(strip)

print numcharsPart1
print numcharsPart2