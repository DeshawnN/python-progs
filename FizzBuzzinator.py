num_array = [num for num in range(13)]

def main():

	fizz_counter, buzz_counter, fizzbuzz_counter = [0, 0, 0]
	fizz_nums, buzz_nums, fizzbuzz_nums = [], [], []
	
	print 'Welcome to the FizzBuzzinator!'
	print 'Please enter a two different numbers (from 1 to 12) seperated by a comma  \',\' (and no spaces!): '

	inp = raw_input()

	inp = inp.split(',')

	for num in num_array:
		if inp[0] != num in num_array:
			inp[0] = 3
		if inp[1] != num in num_array:
			inp[1] = 5

	x,y = inp

	x,y = int(x),int(y)

	print 'Now type in any 2 numbers you would like to create a range of seperated by a comma (and no spaces!): '
	inp = raw_input()

	inp = inp.split(',')

	ran1, ran2 = inp
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
				fizzbuzz_counter += 1
				fizzbuzz_nums.append(num)
				fizz_counter += 1
				fizz_nums.append(num)
				buzz_counter += 1
				buzz_nums.append(num)
				
			elif num % y == 0:
				print str(num) + ' Fizz'
				fizz_counter += 1
				fizz_nums.append(num)
				
			elif num % x == 0:
				print str(num) + ' Buzz'
				buzz_counter += 1
				buzz_nums.append(num)
				
			else:
				print num
		else:
			if num % x == 0 and num % y == 0:
				print str(num) + ' FizzBuzz'
				fizzbuzz_counter += 1
				fizzbuzz_nums.append(num)
				fizz_counter += 1
				fizz_nums.append(num)
				buzz_counter += 1
				buzz_nums.append(num)
				
			elif num % x == 0:
				print str(num) + ' Fizz'
				fizz_counter += 1
				fizz_nums.append(num)
				
			elif num % y == 0:
				print str(num) + ' Buzz'
				buzz_counter += 1
				buzz_nums.append(num)
				
			else:
				print num
	print 'Number of Fizz ticks: ' + str(fizz_counter)
	print 'Numbers that Ticked Fizz:', fizz_nums
	print 'Number of Buzz ticks: ' + str(buzz_counter)
	print 'Numbers that Ticked Buzz:', buzz_nums
	print 'Number of FizzBuzz ticks: ' + str(fizzbuzz_counter)
	print 'Numbers that Ticked FizzBuzz:', fizzbuzz_nums
			
main()