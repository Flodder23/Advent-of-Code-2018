from FUNCTIONS import *

def add_velo(star):
	return [[star[0][0] + star[1][0], star[0][1] + star[1][1]], star[1]]

stars = map(open("10_INPUT.txt", "r").read().split("\n"), lambda x: x.split("<")[1:])
stars = map(stars, lambda x: map(x, lambda y: y.split(">")[:1]))
stars = map(stars, lambda x: map(x, lambda y: map(y[0].split(", "), lambda z: int(z))))
secs = 0
while True:
	secs += 1
	stars = map(stars, lambda x: add_velo(x))
	yo = binary_sort(stars, key = lambda x: x[0][1])
	if yo[-1][0][1] - yo[0][0][1] <= 15:
		print(secs)
		break