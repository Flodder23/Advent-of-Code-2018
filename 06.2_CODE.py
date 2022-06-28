from FUNCTIONS import *

c = map(open("6_INPUT.txt", "r").read().split("\n"), lambda x: map(x.split(", "), key=lambda x: int(x)))
x_order = binary_sort(c, lambda x: x[0])
y_order = binary_sort(c, lambda x: x[1])
c = map(c, lambda x: [x[0] - x_order[0][0], x[1] - y_order[0][1]])

m = [[[None, None] for _ in range(y_order[-1][1])] for _ in range(x_order[-1][0])]

r = 0
for x in range(len(m)):
	for y in range(len(m[x])):
		t = 0
		for xc, yc in c:
			t += abs(x-xc) + abs(y-yc)
		r += t < 10000

print(r)