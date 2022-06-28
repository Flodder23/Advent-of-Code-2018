from FUNCTIONS import *

s = open("3_INPUT.txt", "r").read().split("\n")
d = {}
count = 0

for c in s:
	c = c.split()
	coords = c[2][:-1].split(",")
	size = c[3].split("x")
	for x in range(int(size[0])):
		for y in range(int(size[1])):
			ref = str(int(coords[0]) + x + 1) + "," + str(int(coords[1]) + y + 1)
			try:
				if d[ref] == 1:
					count += 1
					d[ref] = 2
				else:
					d[ref] += 1
			except:
				d[ref] = 1
print(count)

