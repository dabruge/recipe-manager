import time

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.unit = ''

    def update_unit(self):
        self.unit = input(f"Enter unit for {self.name}:\n").lower()

    def add_to_list(self, list):
        list.append(self)


def create_ingredient(ingredient_list, given_ingr=False):
    if given_ingr:
        ingr_name = given_ingr
    else:
        ingr_name = input("Enter ingredient name:\n").lower()

    if [ingr for ingr in ingredient_list if ingr.name == ingr_name]:
        print(f"\nIngredient '{ingr_name}' already exists!")
        time.sleep(1.5)
    else:
        new_ingredient = Ingredient(ingr_name)
        new_ingredient.update_unit()
        new_ingredient.add_to_list(ingredient_list)
        return new_ingredient


def list_ingredients(ingredient_list):
    if ingredient_list:
        for ingr in ingredient_list:
            print(f"{ingr.name.capitalize()}     ({ingr.unit})")
    else:
        print("No ingredients saved")
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