import sys

# un dictionnaire de recette contient: des dictionnaire avec 3 key-value:
# ingredients: liste of string
# type de repas: string
# preparation time: entier non negatif
# 
# La clé d'une recette est le nom de la recette # 

class cookbook:
	recipe = {
		"Sandwich" : {
			"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
			"meal" : "lunch",
			"prep_time" : 10
		},
		"Cake" : {
			"ingredients" : ["flour", "sugar", "eggs"],
			"meal" : "dessert",
			"prep_time" : 60
		},
		"Salad" : {
			"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
			"meal" : "lunch",
			"prep_time" : 15
		},
	}

	def print_recipe(self):
		for k, v in self.recipe.items():
			print(k)

	def find_and_print_details(self):
		recipe_name = input('Enter a recipe name\n')
		if (recipe_name in self.recipe):
			Content = self.recipe.get(recipe_name)
			print('ingredients list : {}'.format(Content.get('ingredients')))
			print('To be eaten for {}'.format(Content.get('meal')))
			print('Takes {} minutes of cooking'.format(Content.get('prep_time')))
		else:
			print('recipe \'{}\' not found'.format(recipe_name))
	
	def find_and_delete(self):
		recipe_name = input('Enter a recipe name\n')
		if(recipe_name in self.recipe):
			self.recipe.pop(recipe_name)
		else:
			print('recipe \'{}\' not found'.format(recipe_name))

	def add_new_recipe(self):
		name_recipe = input('What is the name of your new recipe ?\n')
		if (name_recipe in self.recipe):
			print('ERROR: this recipe already exist!')
			return
		self.recipe[name_recipe] = {
			"ingredients" : self.list_ingredients(name_recipe),
			"meal" : input('Enter a meal type:\n'),
			"prep_time" : input('Enter a preparation time: (in minutes)\n')
		}
		while (self.recipe[name_recipe]['prep_time'].isnumeric() == False or int(self.recipe[name_recipe]['prep_time']) < 0):
			self.recipe[name_recipe]['prep_time'] = input('preparation time must be a number, enter an appropriate preparation time\n')

	def list_ingredients(self, name_recipe: str):
		new_list = []
		ingredients = input('Enter ingredients:\n')
		while (ingredients.__len__() > 0):
			new_list.insert(new_list.__len__(), ingredients)
			ingredients = input()
		return new_list

if (__name__ == "__main__"):
	my_cookbook = cookbook()
	choice = input('Welcome to the Python Cookbook !\nList of available option:\n1: Add a recipe\n\
2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n\
5: Quit\nPlease select an option:\n')
	available_option = "12345"
	while(choice != "5"):
		while (choice.__len__() != 1 or available_option.find(choice[0]) == -1):
			choice = input('Sorry, this option does not exist.\nList of available option:\n1: Add a recipe\n\
2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n\
5: Quit\nPlease select an option:\n')
		if (choice == "1"):
			cookbook().add_new_recipe()
		if (choice == "2"):
			cookbook().find_and_delete()
		if (choice == "3"):
			cookbook().find_and_print_details()
		if (choice == "4"):
			cookbook().print_recipe()
		if (choice != "5"):
			choice = input("Please select an option:\n")