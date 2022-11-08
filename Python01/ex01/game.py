class GotCharacter:

	def __init__(self, c_first_name: str = None, c_is_alive: bool = True):
		self.first_name = c_first_name
		self.is_alive = c_is_alive

class Stark(GotCharacter):
	""" The best Family in GoT !"""
	def __init__(self, c_first_name: str = None, c_is_alive: bool = True):
		GotCharacter.__init__(self, c_first_name, c_is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False

	def __str__(self):
		if (self.is_alive == False):
			return 'I am {} {}, my house word is {}, i am dead.'.format(self.first_name, self.family_name, self.house_words)
		else:
			return 'I am {} {}, my house word is {}, i am alive.'.format(self.first_name, self.family_name, self.house_words)

class Targaryen(GotCharacter):
	""" The best Family in House Of Dragons !"""
	def __init__(self, c_first_name: str = None, c_is_alive: bool = True):
		GotCharacter.__init__(self, c_first_name, c_is_alive)
		self.family_name = "Targaryen"
		self.house_words = "We have a lot of Dragons!"

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False

	def __str__(self):
		if (self.is_alive == False):
			return 'I am {} {}, my house word is {}, i am dead.'.format(self.first_name, self.family_name, self.house_words)
		else:
			return 'I am {} {}, my house word is {}, i am alive.'.format(self.first_name, self.family_name, self.house_words)

if (__name__ == "__main__"):
	arya = Stark("Arya")
	print(arya.is_alive)
	arya.die()
	print(arya.is_alive)
	print(arya.__doc__)
	print(arya.__str__())

	arya = Targaryen("Viserys")
	print(arya.is_alive)
	arya.die()
	print(arya.is_alive)
	print(arya.__doc__)
	print(arya.__str__())
