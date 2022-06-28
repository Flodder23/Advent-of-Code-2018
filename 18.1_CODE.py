from FUNCTIONS import *

m = map(open("18_INPUT.txt", "r").read().split("\n"), lambda x: map(list(x), lambda x: [x, x]))
rv = 0
for _ in range(100):
	lrv = rv
	for y in range(len(m)):
		for x in range(len(m[y])):
			t = {".": 0, "|": 0, "#": 0}
			for dy in range(-1, 2):
				for dx in range(-1, 2):
					if not (dy == 0 and dx == 0) and 0 <= y + dy < len(m) and 0 <= x + dx < len(m[y]):
						t[m[y + dy][x + dx][0]] += 1
			if m[y][x][0] == ".":
				if t["|"] >= 3:
					m[y][x][1] = "|"
			elif m[y][x][0] == "|":
				if t["#"] >= 3:
					m[y][x][1] = "#"
			else:
				if t["#"] < 1 or t["|"] < 1:
					m[y][x][1] = "."
	m = map(m, lambda x: map(x, lambda x: [x[1], x[1]]))

	t = {".": 0, "|": 0, "#": 0}
	for y in range(len(m)):
		for x in range(len(m[y])):
			t[m[y][x][0]] += 1
	rv = t["|"] * t["#"]
	print(rv)