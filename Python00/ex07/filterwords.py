import sys

if (__name__ == "__main__"):
	if (sys.argv.__len__() != 3 or sys.argv[1].isnumeric() == True or sys.argv[2].isnumeric() != True):
		print("ERROR")
		exit(1)
	list_to_print = []
	word = ""
	for i in range(sys.argv[1].__len__()):
		if (sys.argv[1][i].isalpha() != True and word.__len__() > int(sys.argv[2])):
			list_to_print.insert(list_to_print.__len__(), word)
			word = ""
		elif (sys.argv[1][i].isalpha() == True):
			word += sys.argv[1][i]
		else:
			word = ""
	if (word.__len__() > int(sys.argv[2])):
		list_to_print.insert(list_to_print.__len__(), word)
	print(list_to_print)
