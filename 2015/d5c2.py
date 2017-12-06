with open('d5_input.txt') as f:
	strings = f.readlines()

nice_strings = 0

for string in strings:
	nice = False
	pair = False
	repeat = False
	
	for i, char in enumerate(string):
		if i < len(string)-3:
			if char == string[i+2]:
				repeat = True
	
		seek = string[i:i+2]
		if  seek in string[i+2:]:
			pair = True
		
	if pair and repeat:
		nice_strings += 1
		
print(nice_strings)
