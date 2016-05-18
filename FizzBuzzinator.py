num_array = [num for num in range(13)]

def main():
	
	print 'Welcome to the FizzBuzzinator!'
	print 'Please enter a two different numbers (from 1 to 12) seperated by a comma  \',\' (and no spaces!): '

	inp = raw_input()

	x,y = inp.split(',')

	x,y = int(x),int(y)

	print 'Now type in any 2 numbers you would like to create a range of seperated by a comma (and no spaces!): '
	inp = raw_input()

	ran1, ran2 = inp.split(',')
	ran1, ran2 = int(ran1), int(ran2)
	
	if ran1 > ran2 and ran1 <= 101:
		_range = range(ran1, ran2, -1)
	elif ran2 > ran1 and ran2 <= 101:
		_range = range(ran1, ran2)
	elif ran1 > ran2 and ran1 >= 101:
		_range = xrange(ran1, ran2, -1)
	else:
		_range = xrange(ran1, ran2)

	for num in _range:
		if x > y:
			if num % y == 0 and num % y == 0:
				print str(num) + ' FizzBuzz'
			elif num % y == 0:
				print str(num) + ' Fizz'
			elif num % x == 0:
				print str(num) + ' Buzz'
			else:
				print num
		else:
			if num % x == 0 and num % y == 0:
				print str(num) + ' FizzBuzz'
			elif num % x == 0:
				print str(num) + ' Fizz'
			elif num % y == 0:
				print str(num) + ' Buzz'
			else:
				print num
			
main()