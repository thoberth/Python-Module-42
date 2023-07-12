import sys
import os
sys.path.append(os.path.abspath("../ex01"))
from ImageProcessor import *
from PIL import Image
import numpy as np

class ColorFilter:
	def __init__(self):
		pass

	def invert(self, array):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		new_arr = np.copy(array)
		new_arr[..., :3] = 255 - new_arr[..., :3]
		return new_arr

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		new_arr = np.zeros(array.shape, dtype="uint8")
		new_arr[..., 2:] = array[..., 2:]
		return new_arr

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		new_arr = np.copy(array)
		new_arr[..., 0::2] = 0
		return new_arr

	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		new_arr = array - (self.to_blue(array) + self.to_green(array))
		new_arr[..., 3:] = array[..., 3:]
		return new_arr

	def to_celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		bounds = np.arange(array.min(), array.max(), int(255/5))
		res = array.copy()
		lower_bound = bounds[0]
		for upper_bound in bounds[1:]:
			mask = (res[..., :3] > lower_bound) & (res[..., :3] < upper_bound)
			res[..., :3][mask] = lower_bound
			lower_bound = upper_bound
		return res

	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = ’mean’/’m’: performs the mean of RBG channels.
		For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not type(array) is np.ndarray:
			print("Error, argument array is not a np.ndarray")
			return None
		if (filter not in ["m", "mean", "w", "weight"]):
			print("Error, filter argument must contain 'm', 'mean', 'w', 'weight'")
		if filter in ['m', 'mean'] and len(kwargs) != 0:
			print('Error, with \'m\', \'mean\' argument it must be 0 kwargs')
		elif filter in ['w', 'weight']:
			to_verif = list(kwargs.values())[0]
			if len(kwargs) != 1 or list(kwargs.keys())[0] not in ["w", "weight"] or len(to_verif) != 3 or \
				not all(isinstance(v, float) for v in to_verif) or np.sum(to_verif) != 1:
				print("Error, kwargs is invalid")
		new_arr = None
		if filter in ['m', 'mean']:
			new_arr = np.sum(array[..., :3], axis=2, keepdims=True, dtype="uint8") / 3
			new_arr = np.reshape(new_arr, (new_arr.shape[0], new_arr.shape[1]))
		else:
			new_arr = np.sum(array[..., :3] * list(kwargs.values())[0], axis=2, keepdims=True, dtype="uint8") / 3
			new_arr = np.reshape(new_arr, (new_arr.shape[0], new_arr.shape[1]))
		return new_arr


if __name__=="__main__":
	ip = ImageProcessor()
	cf = ColorFilter()
	im1 = ip.load("../42AI.png")
	im2 = ip.load("../elon_canaGAN.png")
	im3 = ip.load("../IMG_2803 - copie.png")
	ip.display(cf.invert(im1))
	# ip.display(cf.invert(im2))
	# ip.display(cf.to_blue(im1))
	# ip.display(cf.to_blue(im2))
	# ip.display(cf.to_green(im1))
	# ip.display(cf.to_green(im2))
	# ip.display(cf.to_red(im1))
	# ip.display(cf.to_red(im2))
	# ip.display(cf.to_celluloid(im1))
	# ip.display(cf.to_celluloid(im2))
	# ip.display(cf.to_celluloid(im3))
	# ip.display(cf.to_grayscale(im1, "m"))
	# ip.display(cf.to_grayscale(cf.to_blue(im2), "m"))
	# ip.display(cf.to_grayscale(cf.to_green(im2), "m"))
	# ip.display(cf.to_grayscale(cf.to_red(im2), "m"))
	# ip.display(cf.to_grayscale(im2, "w", w = [1., 0. , 0.]))
	# ip.display(cf.to_grayscale(im2, "w", w=[0., 1., 0.]))
	# ip.display(cf.to_grayscale(im2, "w", w=[0., 0., 1.]))
	ip.display(cf.to_grayscale(cf.to_celluloid(im3), "weight", weight = [1., 0., 0.]))