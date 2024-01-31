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
		print("Error {} never won medals".format(country))
		return None
	# sport_to_sort = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton',
	# 	'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
	# 	'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming',
	# 	'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
	res = {}
	for year in set(df['Year'].tolist()):
		if year not in res.keys():
				res.update({year: {'G':0,'S':0,'B':0}})
	df = df[(df["NOC"] == country)].dropna(subset=['Medal'])

	# remove from df the year/event identical to keep only one players e.g. 'Basketball man' -> 2000
	df = df.drop_duplicates(['Games', 'Event'], keep='first')
	for index, row in df.iterrows():
		medal = row['Medal']
		sport = row['Sport']
		year = row['Year']
		if year==1952 :
			print(medal, '\t',sport)
		if medal == "Gold":
			res[year]['G'] += 1
		if medal == "Silver":
			res[year]['S'] += 1
		if medal == "Bronze":
			res[year]['B'] += 1
	return res

if __name__=="__main__":
	res = how_many_medals_by_country(pd.read_csv("../athlete_events.csv"), 'ALB')
	if res != None:
		[print(key, value) for key, value in res.items()]
	# check on internet the result
