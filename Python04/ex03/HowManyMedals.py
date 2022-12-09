import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
from FileLoader import *

def how_many_medals(df, name):
	if not (isinstance(df, pd.DataFrame) and isinstance(name, str)):
		print("Error in argument")
		return None
	if name not in df["Name"].values:
		print("Error {} hasn't been found in the DataFrame!".format(name))
	res = {}
	df = df[(df["Name"] == name)]
	for index, row in df.iterrows():
		year = row['Year']
		medal = row['Medal']
		if year not in res.keys():
			res.update({year : {"G": 0, "S": 0, "B": 0}})
		if medal == "Gold":
			res[year]['G'] += 1
		if medal == "Silver":
			res[year]['S'] += 1
		if medal == "Bronze":
			res[year]['B'] += 1
	return res

if __name__=="__main__":
	fl = FileLoader()
	data = fl.load("../athlete_events.csv")
	print("Per Knut Aaland")
	[print(key, value) for key, value in how_many_medals(data, "Per Knut Aaland").items()]
	print("Kjetil Andr Aamodt")
	[print(key, value)
            for key, value in how_many_medals(data, "Kjetil Andr Aamodt").items()]
	print("Lowell Conrad Bailey")
	[print(key, value)
            for key, value in how_many_medals(data, "Lowell Conrad Bailey").items()]
	print("Usain St. Leo Bolt")
	[print(key, value)
            for key, value in how_many_medals(data, "Usain St. Leo Bolt").items()]
