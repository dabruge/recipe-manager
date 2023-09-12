import os
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
    # might need to refactor so same ingredient cant appear in receipe twice
    add_more_ingr = True
    recipe_name = input("Enter recipe name:\n").lower()
    new_recipe = Recipe(recipe_name)
    new_ingredient = ''
    while add_more_ingr:
        choice = ''
        if [rec for rec in recipe_list if rec.name == new_recipe.name]:
            print(f"\nRecipe '{recipe_name}' already exists! Use the Edit recipe option")
            time.sleep(1.5)
        else:
            ingr_name = input("\nEnter ingredient:\n")
            existing_ingr = [ingr for ingr in ingredient_list if ingr.name == ingr_name]
            if existing_ingr:
                ingr_qty = input(f"\nEnter quantity for {ingr_name} (in {existing_ingr[0].unit}):\n")
                new_recipe.add_ingredient(existing_ingr[0], ingr_qty)
            else:
                # ingredient does not exist
                print(f"\nIngredient '{ingr_name}' does not exist! Adding ingredient now:\n")
                new_ingredient = create_ingredient(ingredient_list, ingr_name)
                ingr_qty = input(f"\nEnter quantity of {ingr_name} (in {new_ingredient.unit}) for {new_recipe.name}:\n")
                new_recipe.add_ingredient(new_ingredient, ingr_qty)

            while choice not in ['y', 'n']:
                os.system('clear')
                print(f"{new_ingredient.name} added for {new_recipe.name}\n")
                choice = input("Add another ingredient? [y/n]\n").lower()
                if choice == 'n':
                    add_more_ingr = False
    new_recipe.add_to_list(recipe_list)


def list_recipes(recipe_list):
    if recipe_list:
        for recipe in recipe_list:
            print(recipe.name.capitalize())
    else:
        print("No recipes saved")

def edit_recipe(recipe_list):
    if recipe_list:
        chosen_recipe = ''
        while True:
            os.system('clear')
            print("Recipes:\n")
            list_recipes(recipe_list)
            chosen_recipe = input("\nPlease enter recipe name to edit:\n").lower()
            if chosen_recipe == 'exit':
                break
            if chosen_recipe not in [rec.name for rec in recipe_list if rec.name == chosen_recipe]:
                print(f"\nRecipe '{chosen_recipe}' does not exist, choose an existing one!")
                print("Or enter 'exit' to return to menu")
                time.sleep(1)
            else:
                break
        for recipe in recipe_list:
            if recipe.name == chosen_recipe:
                print(f"\n{recipe.name.capitalize()}\n")
                for ingr in recipe.ingredients:
                    print(ingr['quantity'], ingr['ingredient'].unit, ingr['ingredient'].name)
                time.sleep(4)
        
    else:
        print("No recipes saved")
        time.sleep(1.5)