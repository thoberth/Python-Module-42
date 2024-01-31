import os
import sys
sys.path.append(os.path.abspath("../../Python04/ex00"))
import pandas as pd
def yougest_fellah(df, oYear):
	if not isinstance(df, pd.core.frame.DataFrame) or not isinstance(oYear, int):
		print("Error parameter type are wrong")
		return None
	res = {"f" : None, "m": None}
	try:
		res['f'] = df.set_index("Year").loc[oYear].set_index("Sex").loc['F']["Age"].min()
		res['m'] = df.set_index("Year").loc[oYear].set_index("Sex").loc['M']["Age"].min()
	except:
		print("Error, while searching in youngest athletes in {}".format(oYear))
	else:
		print(res, "in {}".format(oYear))

if __name__=="__main__":
	try:
		df = pd.read_csv("../athlete_events.csv")
	except:
		print('error with file, verify path')
		exit()
	yougest_fellah(df, 1998)
	yougest_fellah(df, 2004)
	yougest_fellah(df, 1999)
	yougest_fellah(df, 1996)
	yougest_fellah(df, 2000)
	yougest_fellah(df, 1984)
	yougest_fellah(df, 1997)
