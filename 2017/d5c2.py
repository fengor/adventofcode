with open("d5_input.txt") as f:
	jumplines = f.readlines()
	
position = 0
counter = 0
jumps = list()

for jump in jumplines:
    jumps.append(int(jump))

while position > -1 and position < len(jumps):
    start = position
    position += jumps[start]
    counter += 1
    if jumps[start] >= 3:
        jumps[start] -= 1
    else:
        jumps[start] += 1

print(counter)
