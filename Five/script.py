import re
nicestrings = 0

with open("input.txt", "r") as f:
	for line in f:
		vowels = re.search("(.*?[a,e,i,o,u].*?){3}", line)
		double = re.findall(r'([a-z])\1', line)
		naughty = re.search("ab|cd|pq|xy", line)

		repeatingdouble = re.findall(r"([a-z]{2}).*\1", line)
		sandwich = re.findall(r"([a-z]).\1", line)

		if repeatingdouble and sandwich:
			nicestrings += 1
print nicestrings
