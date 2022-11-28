import numpy
from PIL import Image

class ImageProcessor:
	def __init__(self):
		pass

	@staticmethod
	def load(path):
		if not isinstance(path, str):
			print("Error, path must be a string!")
			return None
		r = None
		try:
			r = numpy.asarray(Image.open(path))
		except:
			print("Error, Can't read or open file : \"{}\"!".format(path))
		else:
			print("Loading image {} of dimension {} {}".format(path, r.shape[0], r.shape[1])) 
		return(r)

	@staticmethod
	def display(array):
		if not type(array) is numpy.ndarray:
			print("Error, argument must be an array")
			return None
		print("opening image:")
		img = Image.fromarray(array)
		img.show()

if __name__=="__main__":
	ip = ImageProcessor()
	im1 = ip.load('../42AI.png')
	print(im1)
	im2 = ip.load('wrongpath.png')
	im3 = ip.load('../elon_canaGAN.png')
	print(im3)
	print("Display(RGB values of 42AI.png)")
	ip.display(im1)
	print("Display: None")
	ip.display(im2)
	print("Display(RGB values of elon_canaGAN.png)")
	ip.display(im3)