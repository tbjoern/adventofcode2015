def parseLine(line):
	cmd, args = line.split(" ", 1)
	if cmd == "turn":
		val, p1, t, p2 = args.split(" ")
		x1,x2 = p1.split(",")
		y1,y2 = p2.split(",")
		val = 1 if val == "on" else -1
		return (0,val,(int(x1),int(x2)),(int(y1),int(y2)))
	else:
		p1, t, p2 = args.split(" ")
		x1,x2 = p1.split(",")
		y1,y2 = p2.split(",")
		return (1,None,(int(x1),int(x2)),(int(y1),int(y2)))

display = [[0 for x in range(1000)] for y in range(1000)]

with open("input.txt") as f:
	for line in f:
		func, val, p1, p2 = parseLine(line)
		if func == 0:
			for i in range(p1[0],p2[0] + 1):
				for j in range(p1[1], p2[1] + 1):
					display[i][j] += val
					if display[i][j] < 0:
						display[i][j] = 0
		if func	== 1:
			for i in range(p1[0],p2[0] + 1):
				for j in range(p1[1], p2[1] + 1):
					display[i][j] += 2
					if display[i][j] < 0:
						display[i][j] = 0

onpixels = 0
for i in range(1000):
	for j in range(1000):
		onpixels += display[i][j]

print onpixels

