from FUNCTIONS import *

s = open("2_INPUT.txt", "r").read().split("\n")
for a in range(len(s)):
	for b in range(a + 1, len(s)):
		d = 0
		out = ""
		for c in range(len(s[a])):
			if s[a][c] == s[b][c]:
				out += s[a][c]
			else:
				d += 1
			if d >= 2:
				break
		if d == 1:
			print(out)