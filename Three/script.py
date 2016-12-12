x = 0
y = 0
xrobo = 0
yrobo = 0
robo = False
locations = {}

with open("input.txt") as f:
	for line in f:
		for c in line:
			if robo:
				h = (xrobo, yrobo)
			else:
				h = (x,y)
			if not h in locations:
				locations[h] = True
			if robo:
				if c == "^":
					y += 1
				elif c == ">":
					x += 1
				elif c == "<":
					x -= 1
				elif c == "v":
					y -= 1
			else:
				if c == "^":
					yrobo += 1
				elif c == ">":
					xrobo += 1
				elif c == "<":
					xrobo -= 1
				elif c == "v":
					yrobo -= 1
			robo = not robo
print len(locations)