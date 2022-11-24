from inspect import isfunction
def ft_map(function_to_apply, iterable):

	"""Map the function to all elements of the iterable.
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
		yield function_to_apply(iterable[i])

if __name__ == "__main__":
	print(list(ft_map(lambda x: x**x, [1, 2, 3, 4])))
	print(list(map(lambda x: x**x, [1, 2, 3, 4])))
