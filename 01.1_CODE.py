from FUNCTIONS import *

seq = open("1_INPUT.txt", "r").read().split("\n")

tot = 0
for n in seq:
	tot += int(n)
	print(tot)
print(tot)