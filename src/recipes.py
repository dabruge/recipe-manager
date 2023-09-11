import time
from ingredients import Ingredient, create_ingredient, list_ingredients, edit_unit

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self, ingredient, quantity):
        self.ingredients.append({"ingredient": ingredient, "quantity": quantity})

    def add_to_list(self, list):
        list.append(self)


def create_recipe(recipe_list, ingredient_list):
    recipe_name = input("Enter recipe name:\n").lower()
    if [rec for rec in recipe_list if rec.name == recipe_name]:
        print(f"\nRecipe '{recipe_name}' already exists!")
        time.sleep(1.5)
    else:
        new_recipe = Recipe(recipe_name)
        ingr_name = input("\nEnter ingredient:\n")
        existing_ingr = [ingr for ingr in ingredient_list if ingr.name == ingr_name]
        if existing_ingr:
            ingr_qty = input(f"\nEnter quantity for {ingr_name} (in {existing_ingr[0].unit}):\n")
            new_recipe.add_ingredient(existing_ingr[0], ingr_qty)
        else:
            # ingredient does not exist
            print(f"\nIngredient '{ingr_name}' does not exist! Create ingredient now:\n")
            new_ingredient = create_ingredient(ingredient_list)
            ingr_qty = input(f"\nEnter quantity for {ingr_name} (in {new_ingredient.unit}):\n")
            new_recipe.add_ingredient(new_ingredient, ingr_qty)


        new_recipe.add_to_list(recipe_list)

