#This Program can count the number of words in a string or a .txt file.

word_count = 0

def main():
	global word_count
	word_count = 0
	print 'Please enter a String or filename'
	print 'If the file isn\'t in the same directory as the program, be sure to enter the full path! (e.g. C:/xxxx.txt, or E:/xxxxxxx/xxxx.txt'
	string = raw_input()

	if string[-4:] == '.txt':
		read_file(string)
	else:
		for word in string.split():
			if word.isalpha() == True:
				word_count += 1
			else:
				pass

	print 'There are ' + str(word_count) + ' words in that string.'

	reset()


def read_file(file):
	global word_count
	word_count = 0
	f = open(file, 'r')

	for line in f:
		print line
		
	f.close()

	f = open(file, 'r')
	for word in f.read().split():
		word_count += 1

	print 'There are ' + str(word_count) + ' words in that file.'
	f.close()

	reset()

def reset():

	print 'Would you like to count another string? (Press y or n)'

	user_input = raw_input()

	if user_input == 'y':
		main()
	elif user_input == 'n':
		print 'Thank you for trying my program, Goodbye!'
		quit()
	else:
		print 'Invalid input!'
		reset()

main()