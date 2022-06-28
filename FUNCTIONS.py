def search(alist, item, key=lambda x: x, return_pos=True, ignore_pos=False):
	i = key(item)
	pos = 0
	for it in alist:
		if key(it) == i and not pos in ignore_pos:
			if return_pos:
				return True, pos
			else:
				return True
		pos += 1
	if return_pos:
		return False, False
	else:
		return False

def binary_get(alist, item, key):
	lower = 0
	upper = len(alist) - 1
	mid = 0
	i = key(item)
	while lower <= upper:
		mid = (lower + upper) // 2
		m = key(alist[mid])
		if m == i:
			return alist[mid]
		elif m < i:
			lower = mid + 1
		else:
			upper = mid - 1
	return "Could not find item."

def binary_search(alist, item, key=lambda x: x, return_pos=False, ignore_pos=[], needs_sorting=False):
	if len(ignore_pos) != 0:
		new = []
		p = 0
		for i in alist:
			if not p in ignore_pos:
				new.append(i)
			p += 1
		alist = new

	lower = 0
	upper = len(alist) - 1
	mid = 0
	i = key(item)
	while lower <= upper:
		mid = (lower + upper) // 2
		m = key(alist[mid])
		if m == i:
			if return_pos:
				return True, mid
			else:
				return True
		elif m < i:
			lower = mid + 1
		else:
			upper = mid - 1
	if return_pos:
		return False, False
	else:
		return False

def binary_insert(alist, item, key=lambda x : x, duplicate=False, return_duplicate=False):
	lower = 0
	upper = len(alist) - 1
	mid = 0
	i = key(item)
	while lower <= upper:
		mid = (lower + upper) // 2
		m = key(alist[mid])
		if m == i:
			if duplicate:
				alist.insert(mid, item)
			if return_duplicate:
				return alist, True
			else:
				return alist
		elif m < i:
			lower = mid + 1
		else:
			upper = mid - 1
	alist.insert(lower, item)
	if return_duplicate:
		return alist, False
	else:
		return alist

def binary_sort(alist, key=lambda x : x, remove_duplicates=False):
	sorted = []
	for item in alist:
		sorted = binary_insert(sorted, item, key=key, duplicate=not remove_duplicates)
	return sorted

def binary_remove(alist, item, key=lambda x: x, return_found=False):
	lower = 0
	upper = len(alist) - 1
	i = key(item)
	while lower <= upper:
		mid = (lower + upper) // 2
		m = key(alist[mid])
		if m == i:
			del alist[mid]
			if return_found:
				return alist, True
			else:
				return alist
		elif m < i:
			lower = mid + 1
		else:
			upper = mid - 1
	if return_found:
		return alist, False
	else:
		return alist

def map(alist, key=lambda x: x):
	t = []
	for item in alist:
		t.append(key(item))
	return t

def max(alist, key):
	m = None
	for item in alist:
		if m is None or key(item) > key(m):
			m = item
	return m

def min(alist, key):
	m = None
	for item in alist:
		if m is None or key(item) < key(m):
			m = item
	return m