from FUNCTIONS import *

depth = 3879
target = (8, 713)

m = [[0 for _ in range(target[0] + 1)] for _ in range(target[1] + 1)]

e2t = [".", "=", "|"]
y = 0
for x in range(len(m[y])):
	m[y][x] = (x * 16807 + depth) % 20183
x = 0
for y in range(1, len(m)):
	m[y][x] = (y * 48271 + depth) % 20183
for y in range(1, len(m)):
	for x in range(1, len(m[y])):
		m[y][x] = (m[y - 1][x] * m[y][x - 1] + depth) % 20183
m[-1][-1] = depth % 20183
t = 0
for y in range(len(m)):
	for x in range(len(m[y])):
		t += m[y][x] % 3
print(t)