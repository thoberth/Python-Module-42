import sys

morse_dico = {
	"A": ".-" , "B" : "-..." , "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", 'G' : '--.', 'H' : '....', 'I': '..', 'J' : '.---',\
'K': '-.-', 'L' :'.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-',\
'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-',\
'5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.'
	}

if (__name__ == "__main__"):
	if (sys.argv.__len__() < 2):
		print('ERROR: Argument(s) must be space and alphanumeric characters')
		exit(1)
	for i in range(2, sys.argv.__len__()):
		sys.argv[1] += ' '
		sys.argv[1] += sys.argv[i]
	morse = ""
	print(sys.argv[1])
	argument = list(sys.argv[1])
	for i in range(argument.__len__()):
		if (argument[i].isalnum() == False and argument[i] != " "):
			print('ERROR: Argument(s) must be space and alphanumeric characters')
			exit(1)
		if (argument[i] != ' '):
			if (argument[i].islower()):
				argument[i] = argument[i].upper()
			morse += morse_dico.get(argument[i])
		else:
			morse += '/'
		morse += ' '
	print(morse)
