from FUNCTIONS import *

def get_metadata(alist):
	n, m = alist[:2]
	del alist[:2]
	t = 0
	for _ in range(n):
		alist, a = get_metadata(alist)
		t += a
	for _ in range(m):
		t += alist[0]
		del alist[0]

	return alist, t

print(get_metadata(map(open("8_INPUT.txt").read().split(), lambda x: int(x)))[1])