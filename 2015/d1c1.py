with open("C:\\Users\\brac010\\git\\adventofcode\\2015\\d1_input.txt") as f:
	instructions = f.readlines()

floor = 0
	
for c in instructions[0]:
	if c == '(':
		floor += 1
	elif c == ')':
		floor -= 1
	
print(floor)
