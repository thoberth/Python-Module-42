class Recipe:

	def __init__(self, c_name: str, c_cooking_lvl: int, c_cooking_time: int, c_ingredients: list, c_recipe_type: str, c_description : str = ""):
		self.name = c_name # name of the recipe
		if (c_cooking_lvl < 1 or c_cooking_lvl > 5):
			print('Warning: Wrong cooking level, cooking level must between 1 and 5\nBy default cooking level will be 1')
			c_cooking_lvl = 1
		self.cooking_lvl = c_cooking_lvl # range from 1 to 5,
		if (c_cooking_time < 0):
			print('Warning: Wrong cooking time, cooking time must be positive\nBy default cooking time will be 15')
			c_cooking_time = 15
		self.cooking_time = c_cooking_time # in minutes (no negative numbers),
		self.ingredients = c_ingredients # list of all ingredients each represented by a string,
		if (c_recipe_type != "starter" and c_recipe_type != "lunch" and c_recipe_type != "dessert"):
			print('Warning: Wrong recipe type, recipe type must be starter or lunch or dessert\nBy default recipe type will be lunch')
			c_recipe_type = 'lunch'
		self.recipe_type = c_recipe_type # description of the recipe,
		self.description = c_description # can be "starter", "lunch" or "dessert".

	def __str__(self):
		return (self.description + "{} takes {} minute(s) to be cooked, we need {} to cook this {}, cooking level to cook this recipe is {}."
		.format(self.name, self.cooking_time, self.ingredients, self.recipe_type, self.cooking_lvl))
