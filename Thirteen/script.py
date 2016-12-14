import itertools
def extractData(line):
	line = line.split(" ")
	nameaffected = line[0]
	nameNextTo = line[10][:-1]
	namemod = line[2]
	amount = int(line[3])
	if namemod == "lose":
		amount = -1*amount
	return (nameaffected, amount, nameNextTo)

def calcScore(placement, people):
	score = 0
	for i in range(len(placement)):
		left, right = getNeighbors(i, placement)
		if left in people[placement[i]]:
			score += people[placement[i]][left]
		if right in people[placement[i]]:
		 	score += people[placement[i]][right]
	return score

def getNeighbors(index, array):
	return (array[index-1], array[(index+1) % len(array)])

people = {"me": {}}
names = ["me"]

with open("input.txt") as f:
	for line in f:
		line = line.strip()
		nameaffected, amount, nameNextTo = extractData(line)
		if not nameaffected in people:
			people[nameaffected] = {}
		people[nameaffected][nameNextTo] = amount
		if not nameaffected in names:
			names.append(nameaffected)

perms = itertools.permutations(names)
max = 0
for p in perms:
	score = calcScore(p, people)
	if score > max:
		max = score

print max