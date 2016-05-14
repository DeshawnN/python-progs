def main():
	print 'Please enter a string and I\'ll let you know if its a palindrome or not: '
	palindrome = raw_input().lower()

	p_check(palindrome)

def p_check(string):
	is_palindrome = False

	if string == string[::-1]:
		is_palindrome = True
	else:
		pass

	if is_palindrome == True:
		print 'Yes, %s is a Palindrome' %string
	else:
		print 'Sorry, %s isn\'t a palindrome.' %string

	reset()

def reset():
	print 'Try again? press y or n'
	user_input = raw_input() 

	if user_input == 'y':
		main()
	elif user_input == 'n':
		print 'Thanks for trying my program!'
		quit()
	else:
		'Invalid Selection'
		reset()

main()