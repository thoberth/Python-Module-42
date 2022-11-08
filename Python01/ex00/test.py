from book import Book
from recipe import Recipe

if(__name__ == "__main__"):
	cookie = Recipe("Cookie", 2, 15, ("Eggs", "Milk", "Flour", "Chocolate"), "dessert")
	pasta = Recipe("Pasta", 1, 10, ("Water", "Pasta"), "lunch")
	cookBook = Book("my CookBook")
	print('Cookie: -> \n' + cookie.__str__())
	print('Pasta: -> \n' + pasta.__str__())
	print('Add both recipe to my cookBook')
	cookBook.add_recipe(cookie)
	cookBook.add_recipe(pasta)
	print(cookBook.__str__())
	cookBook.add_recipe(1)
	print("get cookie recipe by name :")
	print(cookBook.get_recipe_by_name("Cookie").__str__())

	print("get pasta recipe by type :")
	list_lunch = cookBook.get_recipes_by_types("lunch")
	for i in range(list_lunch.__len__()):
		print(list_lunch[i].__str__())