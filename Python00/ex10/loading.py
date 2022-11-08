import sys
from time import sleep, perf_counter
import os

def ft_progress(listy: range):
	for elem in listy:
		eta = elem * 100/int(listy.stop)
		print('ETA : {:.0f}%'.format(eta), end=" ")
		print('Elapsed time = {:.2f}s'.format(perf_counter() - start), end=" ")
		loading_bar = "["
		for i in range(100):
			if i <= eta:
				loading_bar += '/'
			else:
				loading_bar += ' '
		loading_bar += ']'
		print(loading_bar)
		sleep(0.02)
		os.system('clear')
		yield elem

start = perf_counter()
if (__name__ == "__main__"):
	if (sys.argv.__len__() == 2 and sys.argv[1].isnumeric() == True):
		listy = range(int(sys.argv[1]))
		for elem in ft_progress(listy):
			{}
	else:
		print("Error: argument must be a number!")