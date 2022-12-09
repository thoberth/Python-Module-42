import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
from FileLoader import *

def how_many_medals_by_country(df, country):
	if not (isinstance(df, pd.DataFrame) and isinstance(country, str)):
		print("Error argument are not the right type")
		return None
	if country not in df["NOC"].values:
		print("Error {} never had medals".format(country))
		return None
	res = dict()
	df = df[df["NOC"] == country]
	# remove from df the year/sport identical to keep only one players e.g. 'Basketball' -> 2000
	df.drop_duplicates(subset=['Year', 'Sport'], keep='first', inplace=True)
	for index, row in df.iterrows():
		medal = row['Medal']
		sport = row['Sport']
		year = row['Year']
		if year not in res.keys():
			res.update({year: {'G':0,'S':0,'B':0}})
		if medal == "Gold":
			res[year]['G'] += 1
		if medal == "Silver":
			res[year]['S'] += 1
		if medal == "Bronze":
			res[year]['B'] += 1
	return res

if __name__=="__main__":
	[print(key, value) for key, value in how_many_medals_by_country(FileLoader().load("../athlete_events.csv"), 'FRA').items()]
	# check on internet the result