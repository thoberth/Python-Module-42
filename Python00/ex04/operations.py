import sys

if (sys.argv.__len__() < 3):
	print('Usage: python operations.py <number1> <number2>')
elif (sys.argv.__len__() > 3):
	print('AssertionError: too many arguments')
elif (sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False):
	print('AssertionError: only integers')
else:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print('Sum:\t\t{}'.format(a+b))
	print('Difference:\t{}'.format(a-b))
	print('Product:\t{}'.format(a*b))
	if (b != 0):
		print('Quotient:\t{}'.format(a/b))
		print('Remainder:\t{}'.format(a%b))
	else:
		print('Quotient:\tERROR (division by zero)')
		print('Remainder:\tERROR (modulo by zero)')