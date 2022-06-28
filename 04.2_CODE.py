from FUNCTIONS import *

s = binary_sort(open("4_INPUT.txt", "r").read().split("\n"))

days = []
day = [int(s[0].split()[3][1:])]
for line in s[1:]:
	line = line.split()
	line = [line[1][:-1].split(":"), line[3]]
	if line[1].startswith("#"):
		days.append(day)
		day = [int(line[1][1:])]
	else:
		day.append(int(line[0][1]))
days.append(day)

guards = {}
for day in days:
	if not binary_search(binary_sort(guards.keys()), day[0]):
		guards[day[0]] = [0 for _ in range(61)]
	awake = True
	for a in range(60):
		if len(day) > 1 and a == day[1]:
			del day[1]
			awake = not awake
		if not awake:
			guards[day[0]][a] += 1
			guards[day[0]][-1] += 1

max = [0, 0, 0]
for i in guards.keys():
	for m in range(60):
		if guards[i][m] > max[0]:
			max = [guards[i][m], i, m]

print("%s * %s = %s"%(max[1], max[2], max[1] * max[2]))
