import sys
import random

if (__name__ == "__main__"):
	secret_number = random.randint(1, 99)
	answer = input('This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type \'exit\' to end the game.\n\
Good luck!\n\
What\'s your guess between 1 and 99?\n')
	if (answer == "exit"):
		print('Goodbye!')
		exit(0)
	while(answer.isnumeric() != True):
		answer = input('That\'s not a number.\nWhat\'s your guess between 1 and 99?\n')
		if (answer == "exit"):
			print('Goodbye!')
			exit(0)
	while(int(answer) < 1 or int(answer) > 99):
		answer = input('This number is out of range.\nWhat\'s your guess between 1 and 99?\n')
		if (answer == "exit"):
			print('Goodbye!')
			exit(0)
	count = 1
	while(1):
		if (secret_number == int(answer)):
			if (secret_number == 42):
				print('The answer to the ultimate question of life, the universe and everything is 42.')
			if(count == 1):
				print('Congratulations! You got it on your first try!')
			else:
				print('Congratulations, you\'ve got it!\nYou won in {} attempts!'.format(count))
			exit(0)
		elif(secret_number > int(answer)):
			print('Too low!')
		else:
			print('Too high!')
		answer = input('What\'s your guess between 1 and 99?\n')
		if (answer == "exit"):
			print('Goodbye!')
			exit(0)
		while(answer.isnumeric() != True):
			answer = input('That\'s not a number.\nWhat\'s your guess between 1 and 99?\n')
			if (answer == "exit"):
				print('Goodbye!')
				exit(0)
		while(int(answer) < 1 or int(answer) > 99):
			answer = input('This number is out of range.\nWhat\'s your guess between 1 and 99?\n')
			if (answer == "exit"):
				print('Goodbye!')
				exit(0)
		count += 1