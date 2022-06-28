from FUNCTIONS import *

def move(c, l, d):
	c += d
	if c > l:
		c -= l
	return c

rules = open("9_INPUT.txt", "r").read().split()
players, marbles = int(rules[0]), int(rules[6]) + 1

circle = [0]
scores = [0 for _ in range(players)]
cm = 0
cp = cm - 1

for m in range(cm + 1, marbles):
	if m % 23 == 0:
		a = m
		cm = (cm - 7) % len(circle)
		scores[cp] += a + circle[cm]
		del circle[cm]
	else:
		cm = move(cm, len(circle), 2)
		circle.insert(cm, m)
	cp = (cp + 1) % players
print(max(scores))