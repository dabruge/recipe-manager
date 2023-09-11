class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self, ingredient, quantity):
        self.ingredients.append({"ingredient": ingredient, "quantity": quantity})