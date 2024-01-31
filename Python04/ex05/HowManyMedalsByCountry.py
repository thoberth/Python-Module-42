import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
import pandas as pd
import numpy as np

def how_many_medals_by_country(df, country):
	if not (isinstance(df, pd.DataFrame) and isinstance(country, str)):
		print("Error argument are not the right type")
		return None
	if country not in df["NOC"].values:
		print("Error {} never had medals".format(country))
		return None
	sport_to_sort = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton',
		'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
		'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming',
		'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
	new_array = np.array(str)
	res = dict()
	df = df[df["NOC"] == country]
	# df = df[df["Year"] == 2012]
	# df = df[df["Medal"].isnull() == False]
	for index, row in df.iterrows():
		sport = row["Sport"]
		if sport in sport_to_sort:
			np.append(new_array, 'to_sort')
		else:
			np.append(new_array, 'to_count')
	print(new_array)
	df['to_count'] = new_array.tolist()
	# remove from df the year/event identical to keep only one players e.g. 'Basketball man' -> 2000
	# print(df)
	df.drop_duplicates(subset=['Year'], keep='first', inplace=True)
	# print(df)
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
	[print(key, value) for key, value in how_many_medals_by_country(pd.read_csv("../athlete_events.csv"), 'FRA').items()]
	# check on internet the result
	pass