string = ''

def intro():
	'''
	Prints an introduction message to the screen, takes in user input and assigns it to the global string function, 
	and then calls the string reversing function.
	'''
	global string
	print 'Welcome to my string reverser program'
	print 'With this program you can reverse any string you\'ve entered in the prompt'
	string = raw_input('So Please enter the string you want to reverse: ')

	str_rev()


def str_rev():
	'''
	Pulls the global string function assigned with string assigned by the intro() function, reverses it and 
	'''
	global string
	rev_string = string[::-1]
	print rev_string
	reset()


def reset():
	cont = raw_input('Would you like to reverse another string? (Press y or n): ').lower()

	if cont == 'y':
		intro()
	elif cont == 'n':
		print 'Thanks you for running my program, Goodbye!'
		quit()
	else:
		print 'Invalid selection!'
		reset()


intro()