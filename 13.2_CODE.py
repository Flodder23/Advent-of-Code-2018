from FUNCTIONS import *

def next_coords(x, y, c):
	if   c == ">": return x + 1, y
	elif c == "<": return x - 1, y
	elif c == "^": return x, y - 1
	elif c == "v": return x, y + 1
	else: print("ERROR 0")

pos = lambda x, y: y * 1000 + x

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

while len(carts) > 1:
	crashed = []
	for i in range(len(carts)):
		if not i in crashed:
			x, y, c, d = carts[i]
			nx, ny = next_coords(x, y, c)
			crash, p = search(carts, [nx, ny], key=lambda x: pos(x[0], x[1]), return_pos=True, ignore_pos=crashed)
#			print(crash, p)
			if crash:
#				print("Crash at", map([nx, ny], lambda x: x - 1))
				crashed.append(i)
				crashed.append(p)
#				if len(carts) - len(crashed) <= 1:
#					break
			else:
				if m[ny][nx] == "+":
					nc = turn_direction[c][d]
					nd = next_direction[d]
				else:
					nc = turn_track[c][m[ny][nx]]
					nd = d
				carts[i] = [nx, ny, nc, nd]
	deleted = 0
	for i in binary_sort(crashed):
		del carts[i - deleted]
		deleted += 1
	carts = binary_sort(carts, key=lambda x: pos(x[0], x[1]))
#	print(carts)
#	output = ""
#	for y in range(len(m)):
#		for x in range(len(m[y])):
#			c = binary_get(carts, [x, y], key=lambda x: pos(x[0], x[1]))
#			if c == "Could not find item.":
#				output += m[y][x]
#			else:
#				output += c[2]
#		output += "\n"
#	print(output)

print(carts)