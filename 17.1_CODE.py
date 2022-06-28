from FUNCTIONS import *

def physics(m, c):
	x, y = c
	if m[y][x] == "|":
		dy = 0
		if m[y + 1][x] == ".":
			dy = 1
			while y + dy < len(m) and m[y + dy][x] == ".":
				m[y + dy][x] = "|"
				dy += 1
#			for line in m:
#				print("".join(line))
#			print()
			if y + dy < len(m):
				return physics(m, [x, y + dy - 1])
		elif m[y + 1][x] in ("#", "~"):
			dy = 0
			overflowing = False
			overflowed = False
			while not overflowing:
				todo = [[x, y + dy]]
				sources = []
				for ddx in range(-1, 2, 2):
#					for line in m:
#							print("".join(line))
					dx = ddx
					done = False
					while not done:
						if m[y + dy][x + dx] in (".", "|"):
							if m[y + dy + 1][x + dx] in ("#", "~"):
								todo.append([x + dx, y + dy])
							elif m[y + dy + 1][x + dx] == ".":
								overflowing = True
								done = True
								if m[y + dy + 1][x + dx - ddx] == "#" and not overflowed:
									sources.append(x + dx, y)
									for coords in todo:
										m[coords[1]][coords[0]] = "~"
									m[y + dy][x + dx] = "|"
									physics(m, [x + dx, y + dy])
							elif m[y + dy + 1][x + dx] == "|":
								overflowed = True
						elif m[y + dy][x + dx] == "#":
							done = True
							if overflowing:
								for coords in todo:
									m[coords[1]][coords[0]] = "~"
						dx += ddx
					if not overflowing:
						for coords in todo:
							m[coords[1]][coords[0]] = "~"
					todo = []
				dy -= 1
	return m

i = map(open("17_INPUT.txt", "r").read().split("\n"), lambda x: map(x.split(", "), lambda x: x.split("=")))
s = []
for c in i:
	c[0][1] = int(c[0][1])
	c[1] = map(c[1][1].split(".."), lambda x: int(x))
	if c[0][0] == "x":
		for a in range(c[1][0], c[1][1] + 1):
			s.append([c[0][1], a])
	else:
		for a in range(c[1][0], c[1][1] + 1):
			s.append([a, c[0][1]])

xo = binary_sort(s, lambda x: x[0])
yo = binary_sort(s, lambda x: x[1])
s = map(s, lambda x: [1 + x[0] - xo[0][0], 1 + x[1] - yo[0][1]])

m = [["." for _ in range(3 + xo[-1][0] - xo[0][0])] for _ in range(2 + yo[-1][1] - yo[0][1])]
m[0][501 - xo[0][0]] = "+"
m[1][501 - xo[0][0]] = "|"

for c in s:
	m[c[1]][c[0]] = "#"

physics(m, [501 - xo[0][0], 1])

print()
for line in m:
	print("".join(line))