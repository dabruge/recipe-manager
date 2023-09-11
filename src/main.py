import os
import time
from ingredients import Ingredient, create_ingredient, list_ingredients, edit_unit
from recipes import Recipe, create_recipe
from menus import main_menu, ingredients_menu, recipes_menu, shopping_list_menu

def main():
    saved_ingredients = []
    saved_recipes = []
    while True:
        main_choice = main_menu()
        match main_choice:
            case '1':
                while True:
                    ingredient_choice = ingredients_menu()
                    match ingredient_choice:
                        case '1': # add new ingredient
                            os.system('clear')
                            create_ingredient(saved_ingredients)
                        case '2': # view saved ingredients
                            os.system('clear')
                            list_ingredients(saved_ingredients)
                        case '3': # edit ingredient unit
                            os.system('clear')
                            edit_unit(saved_ingredients)
                        case '4':
                            break
            case '2':
                while True:
                    recipe_choice = recipes_menu()
                    match recipe_choice:
                        case '1': # add new recipe
                            os.system('clear')
                            create_recipe(saved_recipes, saved_ingredients)
                        case '2': # view saved recipes
                            pass
                        case '3': # edit recipe
                            pass
                        case '4': # delete recipe
                            pass
                        case '5':
                            break
            case '3':
                while True:
                    list_choice = shopping_list_menu()
                    match list_choice:
                        case '1': # select recipe
                            pass
                        case '2': # view selected recipes
                            pass
                        case '3': # view shopping list
                            pass
                        case '4':
                            break
            case '4':
                os.system('clear')
                print("\nClosing the program")
                print("\nGoodbye!\n")
                time.sleep(1.5)
                os.system('clear')
                break


if __name__ == "__main__":
    main()