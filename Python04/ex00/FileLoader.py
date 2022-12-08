import pandas as pd

class FileLoader:
	def __init__(self): # do nothing
		pass

	def load(self, path):
		"""
		Displays a message specifying the dimension of the dataset
		Args:
		-----
		path: the path to the dataset to load
		Return:
		-----
		The dataset loaded as a pandas.DataFrame
		None if error occured
		"""
		if not isinstance(path, str):
			print("Error, path is not a str!")
			return None
		try:
			df = pd.read_csv(path)
		except:
			print("Error while opening the file, file could be corrupted or path is wrong")
			return None
		print("The dimension of the DataFrame is {}".format(df.shape))
		return df

	def display(self, df, n):
		"""
		displays the first n rows of the dataset if n is positive,
		or the last n rows if n isnegative.
		Args:
		-----
		df: a pandas.DataFrame to displays
		n: an integers
		Return:
		-----
		None
		"""
		if not isinstance(df, pd.core.frame.DataFrame) or not isinstance(n, int):
			print("Error, the parameter(s) are wrong!")
			return None
		if n > 0:
			print(df.head(n))
		else :
			print(df.tail(abs(n)))


if __name__=="__main__":
	fl = FileLoader()
	fl.display(fl.load("../athlete_events.csv"), 10)