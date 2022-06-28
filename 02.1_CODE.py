from FUNCTIONS import *

s = open("2_INPUT.txt", "r").read().split("\n")
d = {}
a = "abcdefghijklmnopqrstuvwxyz"
contain_2 = 0
contain_3 = 0
for k in a:
		d[k] = 0

for i in s:
	for l in i:
		d[l] += 1
	done_2 = False
	done_3 = False
	for k in a:
		if not done_2 and d[k] == 2:
			contain_2  += 1
			done_2 = True
		if not done_3 and d[k] == 3:
			contain_3 += 1
			done_3 = True
		d[k] = 0

print(contain_2 * contain_3)