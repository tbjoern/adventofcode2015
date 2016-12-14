import re
import sys
pw = "abcdefgh" if len(sys.argv) == 1 else sys.argv[1]

def incLetter(x):
	val = ord(x) - ord('a')
	val += 1
	overflow = False
	if val % 26 == 0:
		overflow = True
		val = 0
	val += ord('a')
	return (chr(val), overflow)

def incString(s):
	index = len(s) - 1
	incChar = ('',True)
	while incChar[1] and index >= 0:
		incChar = incLetter(s[index])
		s = s[:index] + incChar[0] + s[index+1:]
		index -= 1
	return s

def hasTriplet(s):
	prev = s[0]
	count = 1
	for c in s:
		if incLetter(prev)[0] == c and prev != 'z':
			count += 1
			if count == 3:
				return True
		else:
			count = 1
		prev = c
	return False

def notBad(s):
	return not 'i' in s and not 'o' in s and not 'l' in s

def hasPairs(s):
	matches = re.findall(r"(.)\1", s)
	if matches:
		first = matches[0]
		for m in matches:
			if first != m:
				return True
	return False

print pw
foundNewPassword = False
while not foundNewPassword:
	pw = incString(pw)
	foundNewPassword = hasTriplet(pw) and notBad(pw) and hasPairs(pw)
print pw