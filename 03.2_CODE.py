from FUNCTIONS import *

s = open("3_INPUT.txt", "r").read().split("\n")
#s = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
d = {}
u = []
intacts = []
count = 0

for c in s:
	c = c.split()
	i = c[0][1:]
	coords = c[2][:-1].split(",")
	size = c[3].split("x")
	intact = True
	for x in range(int(size[0])):
		for y in range(int(size[1])):
			ref = str(int(coords[0]) + x + 1) + "," + str(int(coords[1]) + y + 1)
			try:
				if not d[ref] == "gone":
					binary_remove(intacts, d[ref])
					d[ref] = "gone"
				intact = False
			except:
				d[ref] = int(i)
	if intact:
		binary_insert(intacts, int(i))
print(intacts)
