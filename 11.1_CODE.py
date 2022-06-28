from FUNCTIONS import *

s = 3463
g = [[((x + 11) * (y + 1) + s) * (x + 11) for y in range(300)] for x in range(300)]


m = [None, None]
for x in range(len(g)):
	print(x)
	for y in range(len(g[x])):
		t = 0
		sz = 300 - max(x, y)
		for p in range(sz):
			for xp in range(0, p - 1):
				t += g[x + xp][y]
			for yp in range(0, p):
				t += g[x][y + yp]
			t += g[x + p][y + p]
			if m[0] is None or t > m[0]:
				m = [t, [x, y, p]]
print(m)