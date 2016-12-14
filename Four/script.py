import hashlib
import sys

key = "abcdef" if len(sys.argv) == 1 else sys.argv[1]

def hashValid(key, index):
	h = hashlib.md5(key + str(index)).hexdigest()
	if h[:6] == "000000":
		return True
	return False

index = 0
while not hashValid(key,index):
	index += 1
print index