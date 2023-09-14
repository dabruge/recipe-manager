import os

def main_menu():
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        os.system('clear')
        print("Welcome to Recipe Manager\n")
        print("1. Ingredients")
        print("2. Recipes")
        print("3. Shopping list")
        print("4. Exit")
        choice = input("\nPlease enter number of menu selection:\n")
    return choice

def ingredients_menu():
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        os.system('clear')
        print("Ingredients menu\n")
        print("1. Add new ingredient")
        print("2. View saved ingredients")
        print("3. Edit ingredient unit")
        print("4. Back to main menu")
        choice = input("\nPlease enter number of menu selection:\n")
    return choice

def recipes_menu():
    choice = ''
    while choice not in ['1', '2', '3', '4', '5']:
        os.system('clear')
        print("Recipes menu\n")
        print("1. Add new recipe")
        print("2. View saved recipes")
        print("3. Edit recipe")
        print("4. Delete recipe")
        print("5. Back to main menu")
        choice = input("\nPlease enter number of menu selection:\n")
    return choice

def shopping_list_menu():
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        os.system('clear')
        print("Shopping list menu\n")
        print("1. Select recipe")
        print("2. View selected recipes")
        print("3. View shopping list")
        print("4. Back to main menu")
        choice = input("\nPlease enter number of menu selection:\n")
    return choice

def edit_recipe_menu(recipe_name):
    choice = ''
    while choice not in ['1', '2', '3']:
        os.system('clear')
        print(f"Edit {recipe_name}\n")
        print("1. Edit ingredient quantity")
        print("2. Delete ingredient")
        print("3. Back to Recipe menu")
        choice = input("\nPlease enter number of menu selection:\n")
    return choice
