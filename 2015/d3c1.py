with open("d3_input.txt") as f:
	directions = f.readlines()

visited = set()
x, y = 0, 0

visited.add(str(x)+','+str(y))

for step in directions[0]:
	if step == '^':
		y += 1
	elif step == '>':
		x += 1
	elif step == '<':
		x -= 1
	elif step == 'v':
		y -= 1
	
	if str(x)+','+str(y) not in visited:
		visited.add(str(x)+','+str(y))
	
print(len(visited))