from collections import Counter
import itertools

with open('d6_input.txt') as f:
	instructions = f.readlines()

lights = [[ False for x in range(1000)] for y in range(1000)]

def toggle(x1, y1, x2, y2, value=None):
	x1 = int(x1)
	y1 = int(y1)
	x2 = int(x2)
	y2 = int(y2)
	
	for x in range(x1,x2+1):
		for y in range(y1, y2+1):
			if value is not None:
				lights[x][y] = value
			else:
				if lights[x][y]:
					lights[x][y] = False
				else: 
					lights[x][y] = True

for instruction in instructions:
	words = instruction.split()
	x1, y1 = words[-3].split(',')
	x2, y2 = words[-1].split(',')
	if words[0] == 'turn' and words[1] == 'on':
		toggle(x1,y1,x2,y2,True)
	if words[0] == 'turn' and words[1] == 'off':
		toggle(x1,y1,x2,y2,True)
	if words[0] == 'toggle':
		toggle(x1,y1,x2,y2)

counter = 0
for row in lights:
	for light in row:
		if light:
			counter += 1
			
print(counter)