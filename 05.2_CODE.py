from FUNCTIONS import *

poly = open("5_INPUT.txt", "r").read()

min = None
for letter in "abcdefghijklmnopqrstuvwxyz":
	p = list(poly)
	i = 1
	while i < len(p):
		#print(p)
		if p[i-1].lower() == letter:
			del p[i-1]
			i = max(0, i-2)
		elif p[i-1].lower() == p[i].lower() and p[i-1] != p[i]:
			del p[i-1:i+1]
			i -= 3
		i += 1
	if p[-1].lower() == letter:
		del p[-1]
	#print(p)
	#print()
	if min is None:
		min = len(p)
	elif min > len(p):
		min = len(p)

print("minimum:", min)