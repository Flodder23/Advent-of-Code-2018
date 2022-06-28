from FUNCTIONS import *

def binary_insert(alist, item):
	lower = 0
	upper = len(alist) - 1
	mid = 0
	while lower <= upper:
		mid = (lower + upper) // 2
		if alist[mid] == item:
			return alist, True
		elif alist[mid] < item:
			lower = mid + 1
		else:
			upper = mid - 1
	alist.insert(lower, item)
	return alist, False


seq = open("1_INPUT.txt", "r").read().split("\n")
tots = [0]
last_tot = 0

done = False
while not done:
	for s in seq:
		tot = last_tot + int(s)
		tots, done = binary_insert(tots, tot)
		if done:
			break
		last_tot = tot
print(tot)