from FUNCTIONS import *

def next_coords(x, y, c):
	if   c == ">": return x + 1, y
	elif c == "<": return x - 1, y
	elif c == "^": return x, y - 1
	elif c == "v": return x, y + 1
	else: print("ERROR 0")

def pos(x, y):
	return y * 1000 + x

cart_shapes = (">", "<", "^", "v")
replace_track = {">": "-", "<": "-", "^": "|", "v": "|"}
turn_track = {">": {"/": "^", "\\": "v", "-": ">"},
			  "<": {"/": "v", "\\": "^", "-": "<"},
			  "^": {"/": ">", "\\": "<", "|": "^"},
			  "v": {"/": "<", "\\": ">", "|": "v"}}
turn_direction = {">": {"l": "^", "f": ">", "r": "v"},
				  "<": {"l": "v", "f": "<", "r": "^"},
				  "^": {"l": "<", "f": "^", "r": ">"},
				  "v": {"l": ">", "f": "v", "r": "<"},}
next_direction = {"l": "f", "f": "r", "r": "l"}
carts = []
m = map(open("13_INPUT.txt", "r").read().split("\n"), lambda x: [" "] + list(x) + [" "])
m = [[" "] * len(m[0])] + m + [[" "] * len(m[0])]
for y in range(1, len(m) - 1):
	for x in range(1, len(m[y]) - 1):
		if m[y][x] in cart_shapes:
			carts.append([x, y, m[y][x], "l"])
			m[y][x] = replace_track[m[y][x]]

print("\n".join(["".join(line) for line in m]))


crashed = False
while not crashed:
	for i in range(len(carts)):
		x, y, c, d = carts[i]
		nx, ny = next_coords(x, y, c)
		if search(carts, [nx, ny], key = lambda x: pos(x[0], x[1])):
			crashed = True
#			print(nx, ny)
			break
		if m[ny][nx] == "+":
			nc = turn_direction[c][d]
			nd = next_direction[d]
		else:
			nc = turn_track[c][m[ny][nx]]
			nd = d
	if crashed:
		break
#	carts = binary_sort(carts, key=lambda x: pos(x[0], x[1]))
#	print(carts)
#	output = ""
#	for y in range(len(m)):
#		for x in range(len(m[y])):
#			c = binary_get(carts, [x, y], key=lambda x: pos(x[0], x[0]))
#			if c == "Could not find item.":
#				output += m[y][x]
#			else:
#				output += c[2]
#		output += "\n"
#	print(output)