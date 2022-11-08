import sys
import string

def text_analyzer(x_str : str = ""):
	'''	This function counts the number of upper characters, lower characters,
			punctuation and spaces in a given text.'''
	if (x_str.__len__() == 0):
		x_str = input('What is the text to analyze?\n')
	if (x_str.isnumeric()):
		print('AssertionError: argument is not a string')
		return
	punct = 0
	upper = 0
	lower = 0
	spaces = 0
	for i in range(x_str.__len__()):
		if(x_str[i].isalpha()):
			if(x_str[i].islower()):
				lower += 1
			else:
				upper += 1
		elif(x_str[i].isspace()):
			spaces += 1
		elif(string.punctuation.find(x_str[i]) != -1):
			punct += 1
	print('The text contains {} character(s):'.format(x_str.__len__()))
	print('- {} upper letter(s)'.format(upper))
	print('- {} lower letter(s)'.format(lower))
	print('- {} punctuation mark(s)'.format(punct))
	print('- {} space(s)'.format(spaces))

if ( (__name__== "__main__") and (sys.argv.__len__() == 2)):
	text_analyzer(sys.argv[1])
else:
	print('AssertionError: Wrong number of argument!')