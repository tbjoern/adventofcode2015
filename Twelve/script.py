import json

rawjason = ""
with open("input.txt") as f:
	rawjason = f.read()

contents = json.loads(rawjason)

def addup(iterable):
	count = 0
	for x in iterable:
		if type(iterable) is dict:
			x = iterable[x]
			if x == "red":
				return 0
		if type(x) is int:
			count += x
		elif type(x) is list:
			count += addup(x)
		elif type(x) is dict:
			count += addup(x)
	return count

print addup(contents)