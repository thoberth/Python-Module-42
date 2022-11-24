import time
from random import randint
import os

# ... your definition of log decorator...
def log(f):
	def f_wrapper(*args, **kwargs):
		fichier = open('machine.log', 'a')
		fichier.write('({})'.format(os.environ['USER']))
		name_func = f.__name__
		name_func = name_func.replace('_', ' ')
		fichier.write('Running: {:19s}'.format(name_func.capitalize()))
		start = time.perf_counter()
		result = f(*args, **kwargs)
		time_exec = time.perf_counter() - start
		if time_exec > 1:
			fichier.write(
				'[ exec-time = {:.3f} s ]\n'.format(time_exec))
		else:
			fichier.write('[ exec-time = {:.3f} ms ]\n'.format(time_exec * 1000))
		fichier.close()
		return result
	return f_wrapper

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)