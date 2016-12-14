import copy
city = {}

def path(start,visited,cities):
	paths = []
	for city in cities[start]:
		if city not in visited:
			nextVisited = copy.copy(visited)
			nextVisited.append(city)
			nextPaths = path(city,nextVisited,cities)
			for p in nextPaths:
				paths.append([start] + p)
	if not paths:
		paths.append([start])
	return paths

def length(path,cities):
	length = 0
	for i in range(1, len(path)):
		length += cities[path[i-1]][path[i]]
	return length

with open("input.txt") as f:
	for line in f:
		c1, x ,c2, y , dist = line.strip().split(" ")
		dist = int(dist)
		if not c1 in city:
			city[c1] = {}
		if not c2 in city:
			city[c2] = {}
		city[c1][c2] = dist
		city[c2][c1] = dist

	min = 0xffffffff
	max = 0
	for start in city:
		paths = path(start,[start],city)
		for p in paths:
			lpath = length(p,city)
			if lpath < min and len(p) == len(city):
				min = lpath
			if lpath > max and len(p) == len(city):
				max = lpath

print min

print max