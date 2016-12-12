total = 0
ribbon = 0

with open("input.txt", "r") as f:
	for line in f:
		x,y,z = line.split("x")
		x = int(x)
		y = int(y)
		z = int(z)
		vals = [x,y,z]
		dims = [x*y, x*z, y*z]
		dims.sort()
		total += 3*dims[0] + 2*dims[1] + 2*dims[2]
		vals.sort()
		ribbon += x*y*z + 2*vals[0] + 2*vals[1]

print total
print ribbon