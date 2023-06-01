import sys

if (len(sys.argv) < 3):
	print('Usage: python operations.py <number1> <number2>')
elif (len(sys.argv) > 3):
	print('AssertionError: too many arguments')
else:
	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except:
		print('AssertionError: only integers')
	print('Sum:\t\t{}'.format(a+b))
	print('Difference:\t{}'.format(a-b))
	print('Product:\t{}'.format(a*b))
	if (b != 0):
		print('Quotient:\t{}'.format(a/b))
		print('Remainder:\t{}'.format(a%b))
	else:
		print('Quotient:\tERROR (division by zero)')
		print('Remainder:\tERROR (modulo by zero)')