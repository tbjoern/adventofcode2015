

init = []
instructions = [] #tuple with cmd, dest, source1, source2

wires = {"b": 46065}

def tryInt(a):
	try:
		return int(a)
	except ValueError as e:
		return a

def get(a, wires):
	if type(a) is str:
		if a in wires:
			return wires[a]
		else:
			wires[a] = 0
			return 0
	else:
		return a

with open("input.txt", "r") as f:
	for line in f:
		sp = line.strip().split(" ")
		l = len(sp)
		if l == 3: # 123 -> x
			instructions.append(("SET", sp[2], tryInt(sp[0]), None))
		elif l == 4: # NOT e -> x
			instructions.append((sp[0], sp[3], tryInt(sp[1]), None))
		elif l == 5:
			instructions.append((sp[1], sp[4], tryInt(sp[0]), tryInt(sp[2])))

def execCmd(instr,wires):
	cmd, dest, p1, p2 = instr
	val = get(dest,wires)
	if cmd == "SET":
		if dest != "b":
			wires[dest] = get(p1,wires)
		#print "SET"
	else:
		if cmd == "AND":
			wires[dest] = get(p1,wires) & get(p2,wires)
		elif cmd == "OR":
			wires[dest] = get(p1,wires) | get(p2,wires)
		elif cmd == "RSHIFT":
			v = get(p1,wires)
			for _ in range(get(p2,wires)):
				v = v >> 1
			wires[dest] = v
		elif cmd == "LSHIFT":
			v = get(p1,wires)
			for _ in range(get(p2,wires)):
				v = v << 1
			wires[dest] = v
		#print cmd
		elif cmd == "NOT":
			wires[dest] = get(p1,wires) ^ 0xffff
	return wires[dest] != val

changed = True
while changed:
	changed = False
	for i in instructions:
		changed = changed or execCmd(i, wires)

#for w in wires:
#	print w + ": " + str(wires[w])

print wires["a"]