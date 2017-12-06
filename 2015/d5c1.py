with open('d5_input.txt') as f:
	strings = f.readlines()

forbidden = ('ab', 'cd', 'pq', 'xy')
vowels = 'aeiou'
nice_strings = 0

for string in strings:
	vowel_count = 0
	double = False
	nice = True
	
	for bad in forbidden:
		if bad in string:
			nice = False
	if not nice:
		continue
		
	for i, char in enumerate(string):
		if char in vowels:
			vowel_count += 1
		if char == string[i-1]: # assume \n as last char
			double = True
	if vowel_count < 3 or not double:
		nice = False
		
	if nice:
		nice_strings += 1
		
print(nice_strings)
