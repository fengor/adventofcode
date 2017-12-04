with open("C:\\eclipse-workspaces\\aoc2017\\d4_input.txt") as f:
	passphrases = f.readlines()
	
good_phrases = 0

for passphrase in passphrases:
	used_words = list()
	good_passphrase = True
	
	for word in passphrase.split():
		if word in used_words:
			good_passphrase = False
		else:
			used_words.append(word)
	
	if good_passphrase:
		good_phrases += 1
	
print(good_phrases)
