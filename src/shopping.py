import os
import time
from recipes import list_recipes

def select_recipe(recipe_list, chosen_recipes):
    if recipe_list:
        chosen_recipe = ''
        while True:
            os.system('clear')
            print("Saved recipes:\n")
            list_recipes(recipe_list)
            chosen_recipe = input("\nPlease enter recipe to add to shopping list:\n").lower()
            if chosen_recipe == 'exit':
                break
            if chosen_recipe not in [rec.name for rec in recipe_list if rec.name == chosen_recipe]:
                print(f"\nRecipe '{chosen_recipe}' does not exist, choose an existing one!")
                print("Or enter 'exit' to return to Shopping List menu")
                time.sleep(2)
            else:
                break
        for recipe in recipe_list:
            if recipe.name == chosen_recipe:
                chosen_recipes.append(recipe)
                print(f"\n{recipe.name.capitalize()} added to shopping list!")
                time.sleep(1.5)
    else:
        print("No recipes saved")
        time.sleep(1.5)

def view_shopping_list(chosen_recipes):
    shopping_list = []
    for recipe in chosen_recipes:
        for ingredient in recipe.ingredients:
            if not any(item['name'] == ingredient.name for item in shopping_list):
                shopping_list.append({"name": ingredient['ingredient'].name, "unit": ingredient['ingredient'].unit, "quantity": ingredient['quantity']})
    print(shopping_list)
    input('\nPress any key to return to menu\n')
