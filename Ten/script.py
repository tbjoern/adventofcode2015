import re
seed = "3113322113"

# number as string
def lookandsay(number):
	count = 0
	prev = number[0]
	result = ""
	for i in number:
		if i == prev:
			count += 1
		else:
			result += str(count) + prev
			prev = i
			count = 1
	result += str(count) + prev
	return result

for _ in range(50):
	seed = lookandsay(seed)

print len(seed)
