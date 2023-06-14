import sys
import random

def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded. '''
	if (option != None and option != "shuffle" and option != "unique" and option != "ordered"):
		print("ERROR: invalid option")
		return
	if (isinstance(text, str) != True or isinstance(sep, str) != True):
		print("ERROR: text or separator is invalid")
		return
	new_list = text.split(sep)
	if (option == "shuffle"):
		random.shuffle(new_list)
	elif (option == "unique"):
		new_list = [x for i, x in enumerate(new_list) if x not in new_list[:i]]
	elif (option == "ordered"):
		new_list.sort()
	for i in new_list:
		yield i

if (__name__ == "__main__"):
	if (len(sys.argv) == 3):
		for word in generator(sys.argv[1], sys.argv[2]):
			print(word)
	elif (len(sys.argv) == 4):
		for word in generator(sys.argv[1], sys.argv[2], sys.argv[3]):
			print(word)
	else:
		print('Usage: python generator.py <text> <separator> <option>')
