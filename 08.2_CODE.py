from FUNCTIONS import *

def get_node_data(alist):
	children, meta = alist[:2]
	del alist[:2]
	total = 0
	if children == 0:
		for _ in range(meta):
			total += alist[0]
			del alist[0]
	else:
		nodes = []
		for _ in range(children):
			alist, a = get_node_data(alist)
			nodes.append(a)
		for _ in range(meta):
			if 0 < alist[0] <= children:
				total += nodes[alist[0] - 1]
			del alist[0]
	return alist, total

print(get_node_data(map(open("8_INPUT.txt").read().split(), lambda x: int(x)))[1])