with open("d3_input.txt") as f:
	directions = f.readlines()

visited = set()
santa_x, santa_y, robo_x, robo_y = 0, 0, 0, 0
active = "santa"

visited.add(str(santa_x)+','+str(santa_y))

def move_santa(step, x, y):
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
	return x, y


for step in directions[0]:
	if active == "santa":
		santa_x, santa_y = move_santa(step, santa_x, santa_y)
		active = "robo"
	else:
		robo_x, robo_y = move_santa(step, robo_x, robo_y)
		active = "santa"
		
print(len(visited))