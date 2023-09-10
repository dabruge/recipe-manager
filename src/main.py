from ingredient import Ingredient
from recipe import Recipe
from menus import main_menu, ingredients_menu, recipes_menu, shopping_list_menu

def main():
    while True:
        main_choice = main_menu()
        match main_choice:
            case '1':
                ingredient_choice = ingredients_menu()
                match ingredient_choice:
                    case '1': # add new ingredient
                        pass
                    case '2': # view saved ingredients
                        pass
                    case '3': # edit ingredient unit
                        pass
                    # case '4':
                    #     pass
            case '2':
                recipe_choice = recipes_menu()
                match recipe_choice:
                    case '1': # add new recipe
                        pass
                    case '2': # view saved recipes
                        pass
                    case '3': # delete recipe
                        pass
                    # case '4':
                    #     pass
            case '3':
                list_choice = shopping_list_menu()
                match list_choice:
                    case '1': # select recipe
                        pass
                    case '2': # view selected recipes
                        pass
                    case '3': # view shopping list
                        pass
                    # case '4':
                    #     pass
            case '4':
                print("\nGoodbye!")
                break



if __name__ == "__main__":
    # ham = Ingredient("ham", "g")
    # bread = Ingredient("bread", "slice")
    # ham_sandwich = Recipe("Ham sandwich")
    # ham_sandwich.add_ingredient(ham.name, ham.unit, 50)
    # ham_sandwich.add_ingredient(bread.name, bread.unit, 2)
    # print(ham_sandwich.name)
    # print(ham_sandwich.ingredients)
    main()