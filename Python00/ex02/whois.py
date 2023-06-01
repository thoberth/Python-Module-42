import sys

def whois(arg):
	if(len(arg) != 2):
		print('AssertionError: more than one argument are provided')
		return
	try:
		x = int(arg[1])
	except :
		print('AssertionError: argument is not an integer')
		return
	x = int(arg[1], 10)
	if (x == 0):
		print('I\'m Zero')
	elif ((x % 2) == 0):
		print('I\'m Even')
	else:
		print('I\'m Odd')

whois(sys.argv)