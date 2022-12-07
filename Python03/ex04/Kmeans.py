import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath("../../Python02/ex03"))
from csvreader import *
import numpy as np

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid  # number of centroids
		self.max_iter = max_iter  # number of max iterations to update the centroids
		self.centroids = []  # values of the centroids

	def fit(self, X): # entrainer le model
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		None.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(X, np.ndarray):
			print("Error, X parameter is not a numpy.ndarray")
			return None
		# choose ncentroid in X randomly to set centroids
		self.centroids = np.random.randint(len(X), size=self.ncentroid)
		self.centroids = X[self.centroids, :]
		# create ncentroid cluster
		self.cluster = [[] for i in range(self.ncentroid)]
		for _ in range(self.max_iter): # restart step 1 & 2 -> max_iter times
			for i in range(len(X)-1): # step 1 = clustering the points with the centroids
				dist = sum(abs((v1) - (v2)) for v1, v2 in zip(self.centroids[0], X[i]))
				n = 0
				# print("i = {}, distance = {}".format(0, dist))
				for i2 in range(1, self.ncentroid):
					dist2 = sum(abs((v1) - (v2)) for v1, v2 in zip(self.centroids[i2], X[i]))
					# print("i = {}, distance = {}".format(i2, dist2))
					if (dist > dist2):
						dist = dist2
						n = i2
				self.cluster[n].append(X[i])
			# step 2 = move the centroid to the mean of their cluster
			for j in range(len(self.centroids[0])):
				for y in range(len(self.cluster)):
					mean = 0.
					for z in range(len(self.cluster[y])):
						mean += (self.cluster[y][z][j])
					if (len(self.cluster[y]) != 0):
						mean /= len(self.cluster[y])
						self.centroids[y][j] = mean
			for element in self.cluster:
				element.clear()

	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(X, np.ndarray):
			print("Error, X parameter is not a numpy.ndarray")
			return None
		return self.centroids

def parsing(**kwargs):
	if not ("filepath" in kwargs and "ncentroid" in kwargs and "max_iter" in kwargs):
		print("Error in program argument")
		exit()
	if not (kwargs["ncentroid"].isnumeric() and kwargs["max_iter"].isnumeric()):
		print("Error in program argument")
		exit()
	return kwargs

if __name__=="__main__":
	if (len(sys.argv) != 4):
		print("Error in program argument")
		exit()
	item = parsing(**dict(arg.split('=') for arg in sys.argv[1:]))
	with CsvReader(item["filepath"], header=True) as csvreader:
		if csvreader == None:
				print("Error with file")
		else:
			header = csvreader.getheader()
			data = csvreader.getdata()
	# list to np.ndarray
	data = np.array(data)
	# modifying the shape by deleting the first element for data
	data = data[:, -3:].astype("float32")

	kmean1 = KmeansClustering(max_iter=int(item["ncentroid"]) , ncentroid=int(item["max_iter"]))
	kmean1.fit(data)
	centroids = kmean1.predict(data)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.scatter(centroids[0][0], centroids[0][1], centroids[0][2])
	plt.show()

# filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
