from inspect import isfunction
def ft_filter(function_to_apply, iterable):

	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if not hasattr(iterable, '__iter__'):
		return None
	if not isfunction(function_to_apply):
		raise TypeError("Error, 1st argument is not a function!")
	for i in range(len(iterable)):
		if function_to_apply(iterable[i]):
			yield iterable[i]

if __name__ == "__main__":
	print(list(ft_filter(lambda dum: not (dum % 2), [1, 2, 3, 4])))
	print(list(filter(lambda dum: not (dum % 2), [1, 2, 3, 4])))
