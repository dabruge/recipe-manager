import os
import time
from ingredients import Ingredient
from recipes import Recipe
from menus import main_menu, ingredients_menu, recipes_menu, shopping_list_menu

def main():
    saved_ingredients = []
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
                            pass
                        case '2': # view saved recipes
                            pass
                        case '3': # delete recipe
                            pass
                        case '4':
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
                print("\nClosing the program\n")
                print("\nGoodbye!\n")
                time.sleep(1.5)
                os.system('clear')
                break

def create_ingredient(ingredient_list):
    new_ingredient = Ingredient()
    if [ingr for ingr in ingredient_list if ingr.name == new_ingredient.name]:
        print(f"\nIngredient '{new_ingredient.name}' already exists!")
        time.sleep(1.5)
    else:
        new_ingredient.update_unit()
        new_ingredient.add_to_list(ingredient_list)

def list_ingredients(ingredient_list):
    for ingr in ingredient_list:
        print(f"{ingr.name}     ({ingr.unit})")
    input('\nPress any key to return to menu\n')

def edit_unit(ingredient_list):
    # this function might later need updating to iterate over recipes that use it to make units consistent
    ingr_to_update = input("\nPlease enter the ingredient to change the unit of:\n")
    for ingr in ingredient_list:
        if ingr.name == ingr_to_update:
            ingr.unit = input(f"\nPlease enter new unit for {ingr.name} (currently {ingr.unit}):\n")
            print("\nUnit updated!")
            time.sleep(1.5)
            return
    print(f"\nIngredient '{ingr_to_update}' does not exist!")
    time.sleep(1.5)


if __name__ == "__main__":
    # ham = Ingredient("ham", "g")
    # bread = Ingredient("bread", "slice")
    # ham_sandwich = Recipe("Ham sandwich")
    # ham_sandwich.add_ingredient(ham.name, ham.unit, 50)
    # ham_sandwich.add_ingredient(bread.name, bread.unit, 2)
    # print(ham_sandwich.name)
    # print(ham_sandwich.ingredients)
    main()