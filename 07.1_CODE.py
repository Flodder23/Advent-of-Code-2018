from FUNCTIONS import *

i = map(map(open("7_INPUT.txt", "r").read().split("\n"), key=lambda x: x.split()), key=lambda x: x[1] + x[7])

before = {}
after = {}
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in a:
	before[letter] = []
	after[letter] = []

for line in i:
	before[line[1]] = binary_insert(before[line[1]], line[0])
	after[line[0]] = binary_insert(after[line[0]], line[1])

order = ""
while len(order) < len(a):
	for letter in a:
		if not binary_search(binary_sort(order), letter) and len(before[letter]) == 0:
			order += letter
			for l in after[letter]:
				before[l] = binary_remove(before[l], letter)
			break
print(order)