from inspect import isfunction
from functools import reduce
def ft_reduce(function_to_apply, iterable):

	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	if not hasattr(iterable, '__iter__'):
		return None
	if not isfunction(function_to_apply):
		raise TypeError("Error, 1st argument is not a function!")
	valeur = iterable[0]
	for i in range(1, len(iterable)):
		valeur = function_to_apply(valeur, iterable[i])
	return valeur

if __name__ == "__main__":
	print(ft_reduce(lambda x, y: x+y, ['H', 'E', 'L', 'L', 'O']))
	print(reduce(lambda x, y: x+y, ['H', 'E', 'L', 'L', 'O']))
