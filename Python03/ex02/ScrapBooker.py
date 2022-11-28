import sys
import os
sys.path.append(os.path.abspath("../ex01"))
from ImageProcessor import *
import numpy as np
from PIL import Image

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dim, position=(0, 0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument \"array\" must be an array")
			return None
		if not (isinstance(dim, tuple) and isinstance(position, tuple) and \
			all(isinstance(v, int) for v in dim) and all(isinstance(v, int) for v in position)) \
			or len(dim) != 2 or len(position) != 2:
			print("Error, argument \"dim\" and \"position\" must be a tuple of 2 integers")
			return None
		if ((dim[0] + position[0]) > array.shape[0] or (dim[1] + position[1]) > array.shape[1]):
			print("Error, combinaison of parameters not compatible")
			return None
		new_arr = array[position[0]: position[0] +
                  dim[0], position[1]: position[1] + dim[1]]
		return new_arr

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument \"array\" must be an array")
			return None
		if axis != 0 and axis != 1:
			print("Error, Axis must be 0 (Horizontal) or 1 (Vertical)")
			return None
		if n <= 0 or (axis == 0 and n >= array.shape[0]) or (axis == 1 and n >= array.shape[1]):
			print("Error, n must be non null positive integer lower than the number of row/column of the array")
			return None
		new_arr = np.delete(array, slice(n-1 , None, n), axis)
		return new_arr

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument \"array\" must be an array")
			return None
		if axis != 0 and axis != 1:
			print("Error, Axis must be 0 (Horizontal) or 1 (Vertical)")
			return None
		if n <= 0:
			print("Error, n must be non null positive integer lower than the number of row/column of the array")
			return None
		new_arr = array
		for _ in range(n - 1):
			new_arr = np.concatenate((new_arr, array), axis)
		return new_arr

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument \"array\" must be an array")
			return None
		if not (len(dim) == 2 and all(isinstance(v, int) for v in dim) and isinstance(dim, tuple)):
			print("Error, argument \"dim\" must be a tuple of 2 integers")
			return None
		new_arr = self.juxtapose(array, dim[0], 0)
		new_arr = self.juxtapose(new_arr, dim[1], 1)
		return new_arr

if __name__== "__main__":
	sb = ScrapBooker()
	ip = ImageProcessor()
	im1 = ip.load("../42AI.png")
	im2 = ip.load("../elon_canaGAN.png")
	ip.display(sb.crop(im1, (100, 200), (100, 0)))
	# ip.display(sb.crop(im2, (int(576/2), int(576/2)), (int(576/2), int(576/2))))
	# ip.display(sb.thin(im1, 100, 0))
	# ip.display(sb.thin(im2, 300, 1))
	# ip.display(sb.juxtapose(im1, 5, 1))
	# ip.display(sb.juxtapose(im2, 3, 1))
	# ip.display(sb.mosaic(im1, (3, 3)))
	# ip.display(sb.mosaic(im2, (5, 2)))
