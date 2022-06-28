from FUNCTIONS import *
from collections import deque

i = open("12_INPUT.txt", "r").read().split("\n")
pots = deque(i[0].split()[2])
rules = []
for r in range(2, len(i)):
	if i[r].split()[-1] == "#":
		rules = binary_insert(rules, i[r].split()[0])
for p in range(len(pots)):
	pots[p] = [pots[p], pots[p], p]

b = 5
for g in range(20):
	while not all([pots[n][0] == "." for n in range(b)]):
		pots.appendleft([".", ".", pots[0][2] - 1])
	while not all([pots[-1 - n][0] == "." for n in range(b)]):
		pots.append([".", ".", pots[-1][2] + 1])
	for p in range(2, len(pots) - 2):
		if binary_search(rules, "".join([pots[p + n][0] for n in range(-2, 3)])):
			pots[p][1] = "#"
		else:
			pots[p][1] = "."
	for p in range(len(pots)):
		pots[p][0] = pots[p][1]

t = 0
for p in pots:
	if p[0] == "#":
		t += p[2]
print(t)