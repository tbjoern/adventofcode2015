f = open("input.txt", "r")
instructions = f.read()
f.close()
floor = 0
pos = 0
stop = False
for line in instructions:
	for c in line:
		pos += 1
		if c == "(":
			floor += 1
		else:
			floor -= 1
		if floor == -1 and not stop:
			print "position: " + str(pos)
			stop = True

print floor