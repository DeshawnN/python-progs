#This Program can count the number of words in a string or a .txt file.

word_count = 0

def main():
	global word_count
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

def read_file(file):
	global word_count
	f = open(file, 'r')

	for word in f.read().split():
		word_count += 1

	print 'There are ' + str(word_count) + ' words in that file.'

main()