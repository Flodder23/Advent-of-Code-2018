from FUNCTIONS import *

i = map(map(open("7_INPUT.txt", "r").read().split("\n"), lambda x: x.split()), lambda x: x[1] + x[7])

before = {}
after = {}
time = {" ": None}
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = 61
for letter in a:
	before[letter] = []
	after[letter] = []
	time[letter] = n
	n += 1

for line in i:
	before[line[1]] = binary_insert(before[line[1]], line[0])
	after[line[0]] = binary_insert(after[line[0]], line[1])

w = [" " for _ in range(5)]
done = ""
t = 0
while len(done) < len(a):
	t += 1
	for j in range(len(w)):
		if w[j] != " ":
			time[w[j]] -= 1
	for j in range(len(w)):
		if time[w[j]] == 0:
			done = "".join(binary_insert(list(done), w[j]))
			for l in after[w[j]]:
				before[l] = binary_remove(before[l], w[j])
			w[j] = " "
	for j in range(len(w)):
		if w[j] == " ":
			for letter in a:
				if len(before[letter]) == 0 and not binary_search(done, letter) and not binary_search(binary_sort(w), letter):
					w[j] = letter
					break
	w = binary_sort(w, duplicate=True)
print(t)