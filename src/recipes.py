class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self, ingredient_name, ingredient_unit, quantity):
        self.ingredients.append({"name": ingredient_name, "unit": ingredient_unit, "quantity": quantity})