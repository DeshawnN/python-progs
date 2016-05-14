def main():
	print 'Welcome to my vowel counting python program.'
	print 'Please enter the string that you wish to count the vowels of: '
	player_input = str(raw_input()).lower()

	vowel_counter(player_input)

def vowel_counter(string):
	vowels = ('a', 'e', 'i', 'o', 'u')
	vowel_count = 0

	for letter in string:
		if letter == letter in vowels:
			vowel_count += 1
		else:
			pass

	print vowel_count

main()