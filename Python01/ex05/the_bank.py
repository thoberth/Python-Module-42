# in the_bank.py
class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


# in the_bank.py
class Bank(object):
	"""The bank
	Its purpose will be to handle the security part of each transfer attempt."""

	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		if (not isinstance(new_account, Account)):
			print("Error, The new account is not a Account Class!")
			return False
		for account in self.accounts:
			if account.name == new_account.name:
				print("Error, The new account cannot have the same name than an other one in the Bank")
				return False
		if (self.accounts.append(new_account)):
			return True
		return False

	def transfer(self, origin, dest, amount):
		""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		if (not (isinstance(origin, str) or isinstance(dest, str) or (isinstance(amount, float) or isinstance(amount, int)))):
			print("Error, Type Error!")
			return False
		if (not amount >= 0):
			print("Error, the amount must be superior than 0")
			return False
		originAccount = None
		destAccount = None
		for account in self.accounts:
			if account.name == origin:
				originAccount = account
			if account.name == dest:
				destAccount = account
		if (originAccount == None or destAccount == None):
			print("Error, an account does not exist in Bank!")
			return False
		if self.verify_account(originAccount) + self.verify_account(destAccount) > 0:
			return False
		if (originAccount.value < amount):
			print("Error,", origin, "do not have enough to make this transfer!")
			return False
		originAccount.transfer(-(amount))
		destAccount.transfer(amount)
		return True

	def verify_account(self, to_verif: Account):
		attribut = vars(to_verif)
		verif_zip = 0
		verif_addr = 0
		for k, v in attribut.items():
			if k[0] == "b":
				print("Error, attribut starting with b in Account of", to_verif.name)
				return 2
			if k.find("zip", 0) != -1:
				verif_zip+=1
			if k.find("addr", 0) != -1:
				verif_addr+=1
		if (verif_zip == 0):
			print("Error, no attribute starting with zip in Account of", to_verif.name)
			return 3
		if (verif_addr == 0):
			print("Error, no attribute starting with addr in Account of", to_verif.name)
			return 8
		if (len(attribut) % 2 == 0):
			print(to_verif.name, "has a even number of attributes")
			return 1
		if not(hasattr(to_verif, 'name') or hasattr(to_verif, 'id') or hasattr(to_verif, 'value')):
			print("Error, {} doesnt have name, id or value in attribute".format(to_verif.name))
			return 4
		if not isinstance(to_verif.name, str):
			print("Error, name is not a str")
			return 5
		if not isinstance(to_verif.id, int):
			print("Error, id is not an id")
			return 6
		if not (isinstance(to_verif.value, int) or isinstance(to_verif.value, float)):
			print("Error, value is not an id or a float")
			return 7
		return 0

	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		print("fix account: ", end="")
		to_fix = None
		for account in self.accounts:
			if account.name == name:
				to_fix = account
		if to_fix == None:
			print("Error, this Account does not exist!")
			return False
		if self.verify_account(to_fix) == 0:
			return True
		a = self.verify_account(to_fix)
		while(a != 0):
			if a == 2:
				for k, v in attribute.items():
					if k.find("b", 0):
						delattr(to_fix, k)
						setattr(to_fix, "new_{}".format(k), v)
			if a == 3:
				setattr(to_fix, "zip", "000-000")
			if a == 8:
				setattr(to_fix, "addr", "An address")
			if a == 1:
				setattr(to_fix, 'new_attr{}'.format(len(vars(to_fix))), None)
			if a == 4:
				if not hasattr(to_fix, "name"):
					setattr(to_fix, "name", "A Name")
				if not hasattr(to_fix, "id"):
					setattr(to_fix, "id", Account.ID_COUNT)
					Account.ID_COUNT+=1
				if not hasattr(to_fix, "value"):
					setattr(to_fix, "value", 0)
			if a == 5:
				to_fix.name = "A Name"
			if a == 6:
				to_fix.id = Account.ID_COUNT
				Account.ID_COUNT+=1
			if a == 7:
				to_fix.value = 0
			a = self.verify_account(to_fix)
		return True


if (__name__ == "__main__"):
	Thomas = Account("Thomas Berthet", value=249.0,
	                 zip='100-345', baddr="221B Baker street")
	Ben = Account("Ben Jacquet", value=300)
	BNP = Bank()

	BNP.add(Thomas)
	BNP.add(Ben)
	print("thomas account = ", Thomas.value, "\nben account =", Ben.value)
	BNP.transfer("Thomas Berthet", "Ben Jacquet", 135)
	print("thomas account = ", Thomas.value, "\nben account =", Ben.value)