import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
import pandas as pd

class SpatioTemporalData:
	def __init__(self, df):
		if not isinstance(df, pd.DataFrame):
			print('Error, argument id not a DataFrame')
			return None
		self.df = df

	def when(self, location):
		if not isinstance(location, str):
			print("Error location is not a string")
			return None
		if location not in self.df.values:
			print("Error {} never had a Olympic Game".format(location))
			return None
		df = self.df[(self.df["City"] == location)]
		res = list()
		for index, row in df.iterrows():
			year = row["Year"]
			if year not in res:
				res.append(year)
		return res

	def where(self, date):
		if not isinstance(date, int):
			print("Error date is not a int")
			return None
		if date not in self.df.values:
			print("Error it never had a Olympic Game in {}".format(date))
			return None
		df = self.df[(self.df["Year"] == date)]
		for index, row in df.iterrows():
			city = row["City"]
			year = row["Year"]
			if year == date:
				return city
		return None


if __name__=="__main__":
	stdata = SpatioTemporalData(pd.read_csv("../athlete_events.csv"))
	print(stdata.when("Barcelona"))
	print(stdata.where(1896))
	print(stdata.when("Paris"))
	print(stdata.where(2016))
	print(stdata.when('Athina'))
