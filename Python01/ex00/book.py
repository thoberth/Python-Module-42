from datetime import datetime
from recipe import Recipe

class Book:

	def __init__(self, c_name: str):
		print('Creating {}....'.format(c_name))
		self.name = c_name
		self.creation_date = datetime.now()
		self.last_update = datetime.now()
		self.recipes_list = {
			"starter" : list(),
			"lunch": list(),
			"dessert": list(),
		}

	def get_recipe_by_name(self, name: str):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for type_lunch in self.recipes_list:
			for i in range(self.recipes_list[type_lunch].__len__()):
				if (self.recipes_list[type_lunch][i].name == name):
					return self.recipes_list[type_lunch][i]
		print('{} do\'nt exist in {}'.format(name, self.name))

	def get_recipes_by_types(self, recipe_type: str):
		"""Get all recipe names for a given recipe_type """
		if (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
			print('{} is an invalid recipe type\nTry with lunch, starter or dessert'.format(recipe_type))
			return
		return self.recipes_list[recipe_type]

	def add_recipe(self, recipe: Recipe):
		"""Add a recipe to the book and update last_update"""
		try:
			self.recipes_list[recipe.recipe_type].append(recipe)
		except AttributeError:
			print("ERROR: only recipe can be add to book")
			return
		last_update = datetime.now()
		print('Adding {} to {} at {}'.format(recipe.name, self.name, self.last_update))

	def __str__(self):
		return("{} was created at {}, last update was at {}".format(self.name, self.creation_date, self.last_update))