from FUNCTIONS import *
from collections import deque

rules = open("9_INPUT.txt", "r").read().split()
players, marbles = int(rules[0]), int(rules[6])
marbles = marbles * 100 + 1

circle = deque([0])
scores = [0 for _ in range(players)]
cp = -1

for m in range(1, marbles + 1):
	if m % 23 == 0:
		circle.rotate(7)
		scores[cp] += m + circle.popleft()
	else:
		circle.rotate(-2)
		circle.appendleft(m)
	cp = (cp + 1) % players
print(max(scores))