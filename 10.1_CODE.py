from FUNCTIONS import *

def add_velo(star):
	return [[star[0][0] + star[1][0], star[0][1] + star[1][1]], star[1]]

stars = map(open("10_INPUT.txt", "r").read().split("\n"), lambda x: x.split("<")[1:])
stars = map(stars, lambda x: map(x, lambda y: y.split(">")[:1]))
stars = map(stars, lambda x: map(x, lambda y: map(y[0].split(", "), lambda z: int(z))))

while True:
	stars = map(stars, lambda x: add_velo(x))
	yo = binary_sort(stars, key = lambda x: x[0][1])
	if yo[-1][0][1] - yo[0][0][1] <= 15:
		big_y = yo[-1][0][1]
		yo = map(yo, key = lambda x: [x[0][0], x[0][1] - yo[0][0][1]])
		xo = binary_sort(stars, key = lambda x: x[0][0])
		xo = map(xo, lambda x: [x[0][0] - xo[0][0][0], x[0][1] - big_y])
		for t in yo:
			print(t)
		output = [["." for _ in range (xo[-1][0] + 1)] for _ in range(yo[-1][1] + 1)]
		for x, y in xo:
			print(x, y, xo[0], yo[0], xo[-1], yo[-1])
			try:
				output[y][x] = "#"
			except:
				print("error")
		for line in output:
			print("".join(line))
		break