from FUNCTIONS import *

c = map(open("6_INPUT.txt", "r").read().split("\n"), lambda x: map(x.split(", "), key=lambda x: int(x)))
#c = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]
x_order = binary_sort(c, key=lambda x: x[0])
y_order = binary_sort(c, key=lambda x: x[1])
c = map(c, lambda x: [x[0] - x_order[0][0], x[1] - y_order[0][1]])

m = [[[None, None] for _ in range(y_order[-1][1])] for _ in range(x_order[-1][0])]

changes = []
n = 1
for p in c:
	m[p[0]][p[1]] = [n, n]
	n += 1
	changes.append(p)

tot_changes = 0

while len(changes) > 0:
	last_changes = changes
	changes = []
	for x, y in last_changes:
		if not m[x][y][0] == 0:
			for nx , ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
				if 0 <= nx < len(m) and 0 <= ny < len(m[nx]) and m[nx][ny][0] is None:
					if m[nx][ny][1] is None:
						m[nx][ny][1] = m[x][y][0]
						changes.append([nx, ny])
					elif m[nx][ny][1] != m[x][y][0]:
						m[nx][ny][1] = 0
	for x, y in changes:
		m[x][y][0] = m[x][y][1]
	tot_changes += len(changes)

m = map(m, lambda x: map(x, lambda x: x[0]))
infinite = []

for y in range(len(m)):
	if m[y][0] != "No": infinite = binary_insert(infinite, m[y][0])
	if m[y][-1] != "No": infinite = binary_insert(infinite, m[y][-1])

for x in range(len(m[0])):
	if m[0][x] != "No": infinite = binary_insert(infinite, m[0][x])
	if m[-1][x] != "No": infinite = binary_insert(infinite, m[-1][x])

totals = {}
for y in range(len(m)):
	for x in range(len(m[y])):
		if m[y][x] != "No" and not binary_search(infinite, m[y][x]):
			if binary_search(binary_sort(totals.keys()), m[y][x]):
				totals[m[y][x]] += 1
			else:
				totals[m[y][x]] = 1
print(max(totals.items(), key=lambda x: x[1]))