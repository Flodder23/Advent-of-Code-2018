from FUNCTIONS import *

p = open("5_INPUT.txt", "r").read()

i = 1
while i < len(p):
	if p[i-1].lower() == p[i].lower() and p[i-1] != p[i]:
		p = p[:i-1] + p[i+1:]
		i -= 3
	i += 1
	
print(len(p))