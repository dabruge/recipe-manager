from ingredient import Ingredient
from recipe import Recipe

if __name__ == "__main__":
    ham = Ingredient("ham", "g")
    bread = Ingredient("bread", "slice")
    ham_sandwich = Recipe("Ham sandwich")
    ham_sandwich.add_ingredient(ham.name, ham.unit, 50)
    ham_sandwich.add_ingredient(bread.name, bread.unit, 2)
    print(ham_sandwich.name)
    print(ham_sandwich.ingredients)
