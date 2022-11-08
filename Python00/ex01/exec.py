import sys

def exec(arg):
	if (arg.__len__() == 1):
		print('Error: no parameter given')
		return
	x = ""
	for i in range(1, arg.__len__()):
		x += " " + arg[i]
	y = ""
	z = ""
	for i in range(x.__len__() - 1, 0, -1):
		if (x[i].isalpha()):
			if(x[i].islower()):
				z = x[i].upper()
			else:
				z = x[i].lower()
			y += z
		else:
			y += x[i]
	print(y)


exec(sys.argv)