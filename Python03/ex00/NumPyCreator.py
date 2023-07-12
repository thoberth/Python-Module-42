import numpy

class NumPyCreator:
	def __init__(self):
		pass

	def from_list(self, lst):
		if not isinstance(lst, list):
			return None
		return numpy.array(lst)

	def from_tuple(self, tpl):
		if not isinstance(tpl, tuple):
			return None
		return numpy.array(tpl)

	def from_iterable(self, itr):
		if not hasattr(itr, '__iter__'):
			return None
		return numpy.array(itr)

	def from_shape(self, shape, value=0): # shape is the number of elements in each dimension
		if not isinstance(shape, tuple):
			return None
		return numpy.full(shape, value, dtype='float64')

	def random(self, shape):
		if not isinstance(shape, tuple):
			return None
		return numpy.random.random(shape)

	def identity(self, n):
		if not (isinstance(n, int) or isinstance(n, float)):
			return None
		return numpy.identity(n)

if __name__=="__main__":
	num = NumPyCreator()
	print("from_list\n", num.from_list([1, 7, 6, 0, 3]))
	print("from_tuple\n", num.from_tuple(([8, 4, 6], [1, 2, 3])))
	list_str = ["yo", "ca", "va"]
	print("from_iterable\n", num.from_iterable([element for element in list_str]))
	print("from_iterable\n", num.from_iterable(range(15)))
	print("from_shape\n", num.from_shape((4, 2), 2))
	print("from_shape\n", num.from_shape((5, 4), 7))
	print("from_shape\n", num.from_shape((4, 2), 7))
	print("random\n", num.random((4, 5)))
	print("identity\n", num.identity(5))
	print(num.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
