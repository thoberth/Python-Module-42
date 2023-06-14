from typing import List

class Evaluator:

	def __init__(self):
		pass

	@staticmethod
	def zip_evaluate(coefs: List, words: List):
		if (coefs.__len__() != words.__len__()):
			return -1
		res = 0.0
		for i in zip(coefs, words):
			res += (i[0] * len(i[1]))
		return res

	@staticmethod
	def enumerate_evaluate(coefs: List, words: List):
		if (coefs.__len__() != words.__len__()):
			return -1
		res = 0.0
		for i, (l_coefs, l_words) in enumerate(zip(coefs, words)):
			res += l_coefs * len(l_words)
		return res

if (__name__ == "__main__"):
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))
	words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))