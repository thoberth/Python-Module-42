class CsvReader(object):
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.is_header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.data = []
		self.header = None

	def __enter__(self):
		print("Enter: opening the file")
		try:
			self.file = open(self.filename, 'r')
		except:
			print("Error while opening the file")
			self.file = None
			return None
		data = list(self.file.read().split('\n'))
		line = data[0]
		self.len = len(list(line.split(self.sep)))
		if self.is_header == True:
			self.header = list(line.split(self.sep))
		to_begin = 1
		if (self.is_header == False):
			to_begin = 0
		to_begin += self.skip_top
		to_end = len(data) - self.skip_bottom
		for i in range(to_begin, to_end):
			new_list = list(str(data[i]).split(self.sep))
			if (self.len != new_list.__len__()):
				if (i == to_end -1 and new_list == [""]):
					break
				return None
			else :
				for i in new_list:
					if i == "":
						return None
				self.data.append(new_list)
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		if self.file != None:
			self.file.close()
		print("Exit: closing the file")

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		return(self.data)

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		return self.header


if __name__ == "__main__":
	def testReader(filename, sep, header, skip_top, skip_bottom):
		with CsvReader(filename, sep, header, skip_top, skip_bottom) as reader:
			if reader == None:
				print("File {} is corrupted or missing".format(filename))
			else:
				print('Header:', reader.getheader(), end="\n")
				print('Data  :', reader.getdata(), end="\n")
	testReader('good.csv', ',', False, 18, 0)
	testReader('good.csv', ',', True, 17, 0)
	testReader('bad.csv', ',', False, 18, 0)
	testReader('bad.csv', ',', True, 17, 0)
	with CsvReader('good.csv') as reader:
		print(reader.getdata())
		print(reader.getheader())

	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")

			# for i, element in enumerate(self.header):
			# 	if element[0] == ' ' or element[0] == '"':
			# 		a = 0
			# 		while (element[a] == ' ' or element[a] == '"' and element[a] != '\0'):
			# 			a+=1
			# 		new_str = ""
			# 		while (element[a] != '"'):
			# 			new_str += element[a]
			# 			a+=1
			# 		self.header[i] = new_str