from typing import List

class Evaluator:

	def __init__(self):
		pass

	@staticmethod
	def zip_evaluate(coefs: List, words: List):
		if (coefs.__len__() != words.__len__()):
			return -1
		result = list(zip(coefs, words))
		sum = 0.0
		for i in result:
			sum += (i[0] * i[1].__len__())
		return sum

	@staticmethod
	def enumerate_evaluate(coefs: List, words: List):
		if (coefs.__len__() != words.__len__()):
			return -1
		l_coefs = list(enumerate(coefs))
		l_words = list(enumerate(words))
		sum = 0.0
		for i in range(l_coefs.__len__()):
			sum += l_coefs[i][1] * l_words[i][1].__len__()
		return sum

if (__name__ == "__main__"):
	words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))