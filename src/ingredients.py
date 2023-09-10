class Ingredient:
    def __init__(self):
        self.name = input("Enter ingredient name:\n").lower()
        self.unit = ''

    def update_unit(self):
        self.unit = input(f"Enter unit for {self.name}:\n").lower()

    def add_to_list(self, list):
        list.append({"name": self.name, "unit": self.unit})