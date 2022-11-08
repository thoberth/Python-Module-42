import sys
import random

def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded. '''
	if (option != None and option != "shuffle" and option != "unique" and option != "ordered"):
		print("ERROR: invalid option")
		return
	if (isinstance(text, str) != True or isinstance(sep, str) != True):
		print("ERROR: text is invalid")
		return
	word = ""
	new_list = []
	for i in text:
		if (i == sep):
			if (word != ""):
				new_list.append(word)
			word = ""
		else:
			word += i
	if (word != ""):
		new_list.append(word)
	if (option == "shuffle"):
		result = []
		while len(new_list) > 0:
			index = random.randrange(0,len(new_list))
			result.append(new_list.pop(index))
		new_list =  result
	elif (option == "unique"):
		i = 0
		while i < new_list.__len__():
			for y in range(i):
				if(new_list[y] == new_list[i]):
					new_list.pop(i)
					i = 0
					break
			i += 1
	elif (option == "ordered"):
		new_list.sort()
	for i in new_list:
		yield i

if (__name__ == "__main__"):
	if (sys.argv.__len__() == 3):
		for word in generator(sys.argv[1], sys.argv[2]):
			print(word)
	else :
		for word in generator(sys.argv[1], sys.argv[2], sys.argv[3]):
			print(word)
