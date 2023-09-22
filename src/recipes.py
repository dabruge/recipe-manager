import os
import time
from ingredients import Ingredient, create_ingredient, list_ingredients, edit_unit
from menus import edit_recipe_menu

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
    recipe_name = input("Enter recipe name:\n").lower()
    new_recipe = Recipe(recipe_name)
    if [rec for rec in recipe_list if rec.name == new_recipe.name]:
        print(f"\nRecipe '{recipe_name}' already exists! Use the Edit recipe option")
        time.sleep(1.5)
    else:
        add_ingredients(new_recipe, ingredient_list)
    new_recipe.add_to_list(recipe_list)


def list_recipes(recipe_list):
    if recipe_list:
        for recipe in recipe_list:
            print(recipe.name.capitalize())
    else:
        print("No recipes found")

def edit_recipe(recipe_list, ingredient_list):
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
                print("Or enter 'exit' to return to Recipe menu")
                time.sleep(2)
            else:
                break
        for recipe in recipe_list:
            if recipe.name == chosen_recipe:
                while True:
                    edit_recipe_choice = edit_recipe_menu(recipe.name)
                    match edit_recipe_choice:
                        case '1': # edit ingredient quantity
                            os.system('clear')
                            edit_qty(recipe)
                        case '2': # add ingredient
                            os.system('clear')
                            add_ingredients(recipe, ingredient_list)
                        case '3': # delete ingredient
                            os.system('clear')
                            delete_ingredient(recipe)
                        case '4': # edit ingredient unit
                            break
    else:
        print("No recipes saved")
        time.sleep(1.5)

def edit_qty(recipe):
    while True:
        os.system('clear')
        print(f"{recipe.name.capitalize()}\n")
        for ingr in recipe.ingredients:
            print(ingr['quantity'], ingr['ingredient'].unit, ingr['ingredient'].name)
        chosen_ingr = input("\nPlease enter ingredient to edit quantity of (or 'exit' to cancel):\n").lower()
        if chosen_ingr == 'exit':
            break
        ingr_instance = [ingr for ingr in recipe.ingredients if ingr['ingredient'].name == chosen_ingr]
        if not ingr_instance:
            print(f"\nIngredient '{chosen_ingr}' does not exist, choose an existing one!")
            print("Or enter 'exit' to return to Edit Recipe menu")
            time.sleep(2)
        else:
            break
    if chosen_ingr != 'exit':
        new_qty = input(f"\nPlease enter new quantity of {chosen_ingr} (in {ingr_instance[0]['ingredient'].unit}):\n")
        for ingr in recipe.ingredients:
            if ingr['ingredient'].name == chosen_ingr:
                ingr['quantity'] = new_qty
    time.sleep(2)

def add_ingredients(recipe, ingredient_list):
    add_more_ingr = True
    while add_more_ingr:
        choice = ''
        ingr_name = input("\nEnter ingredient:\n")
        existing_ingr = [ingr for ingr in ingredient_list if ingr.name == ingr_name]
        if existing_ingr:
            new_ingredient = existing_ingr[0]
            ingr_qty = input(f"\nEnter quantity for {ingr_name} (in {existing_ingr[0].unit}):\n")
            recipe.add_ingredient(existing_ingr[0], ingr_qty)
        else:
            # ingredient does not exist
            print(f"\nIngredient '{ingr_name}' does not exist! Adding ingredient now:\n")
            new_ingredient = create_ingredient(ingredient_list, ingr_name)
            ingr_qty = input(f"\nEnter quantity of {ingr_name} (in {new_ingredient.unit}) for {recipe.name}:\n")
            recipe.add_ingredient(new_ingredient, ingr_qty)

        while choice not in ['y', 'n']:
            os.system('clear')
            print(f"{new_ingredient.name.capitalize()} added for {recipe.name.capitalize()}\n")
            choice = input("Add another ingredient? [y/n]\n").lower()
            if choice == 'n':
                add_more_ingr = False

def delete_ingredient(recipe):
    while True:
        os.system('clear')
        print(f"{recipe.name.capitalize()}\n")
        for ingr in recipe.ingredients:
            print(ingr['quantity'], ingr['ingredient'].unit, ingr['ingredient'].name) # maybe change listing ingredients to a Recipe method
        chosen_ingr = input("\nPlease enter ingredient to delete from recipe (or 'exit' to cancel):\n").lower()
        if chosen_ingr == 'exit':
            break
        ingr_instance = [ingr for ingr in recipe.ingredients if ingr['ingredient'].name == chosen_ingr]
        if not ingr_instance:
            print(f"\nIngredient '{chosen_ingr}' does not exist, choose an existing one!")
            print("Or enter 'exit' to return to Edit Recipe menu")
            time.sleep(2)
        else:
            for ingr in recipe.ingredients:
                if ingr['ingredient'].name == chosen_ingr:
                    recipe.ingredients.remove(ingr)
            print(f"\n{chosen_ingr.capitalize()} removed!")
            time.sleep(2)
            break

def delete_recipe(recipe_list):
    while True:
        os.system('clear')
        print("Saved recipes:\n")
        list_recipes(recipe_list)
        recipe_to_delete = input("\nPlease enter name of recipe to delete (or 'exit' to cancel):\n").lower()
        if recipe_to_delete == 'exit':
            break
        recipe_instance = [recipe for recipe in recipe_list if recipe.name == recipe_to_delete]
        if not recipe_instance:
            print(f"\nRecipe '{recipe_to_delete}' does not exist, choose an existing one!")
            print("Or enter 'exit' to return to Recipe menu")
            time.sleep(2)
        else:
            for recipe in recipe_list:
                if recipe.name == recipe_to_delete:
                    recipe_list.remove(recipe)
            print(f"\n{recipe_to_delete.capitalize()} removed!")
            time.sleep(2)
            break
            