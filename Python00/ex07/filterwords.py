import sys

if (__name__ == "__main__"):
	if (len(sys.argv) != 3 or sys.argv[1].isnumeric() == True or sys.argv[2].isnumeric() != True):
		print("ERROR")
		exit(1)
	word_len = int(sys.argv[2])
	str_to_print = ''.join([c for c in sys.argv[1] if c.isalnum() == True or c == ' '])
	list_to_print = [word for word in str_to_print.split(' ') if len(word) > word_len]
	print(list_to_print)
