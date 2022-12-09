import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
from FileLoader import *

def proportion_by_sport(df, oYear, sport, gender):
	if not (isinstance(df, pd.DataFrame) and isinstance(oYear, int) and\
		isinstance(sport, str)) or (gender != "M" and gender != "F"):
		print("Error in argument")
		return None
	if (sport not in df["Sport"].values):
		print("There is no |{}| column in this DataFrame".format(sport))
		return None
	try:
		res = df.set_index("Year").loc[oYear].set_index("Sport").loc[sport]
		print((res['Sex']==gender).mean())
	except BaseException as e:
		print("Error while searching in DataFrame, no data for {} in {}".format(sport, oYear))

if __name__=="__main__":
	fl = FileLoader()
	df = fl.load("../athlete_events.csv")
	proportion_by_sport(df, 2004, 'Tennis', "F")
	proportion_by_sport(df, 2004, 'Tennis', "M")
	proportion_by_sport(df, 1997, 'Basketball', "M")
	proportion_by_sport(df, 1997, 'Basketball', "F")
	proportion_by_sport(df, 2000, 'Judo', "M")
	proportion_by_sport(df, 2000, 'Judo', "F")
