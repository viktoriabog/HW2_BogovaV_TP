class Ingredient:

    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter

    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return (
            f"{self.name}: "
            f"{self.quantity} {self.unit}"
        )
    def __repr__(self):
        return (
            f"Ingredient("
            f"'{self.name}', "
            f"{self.quantity}, "
            f"'{self.unit}')"
        )

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return (
            self.name == other.name
            and self.unit == other.unit
        )

class Recipe:
    def __init__(
        self,
        title: str,
        ingredients=None
    ):
        self.title = title
        self.ingredients = (
            ingredients[:]
            if ingredients
            else []
        )

    def add_ingredient(
        self,
        ingredient: Ingredient):

        for current in self.ingredients:

            if current == ingredient:
                current.quantity += (
                    ingredient.quantity)
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return (
            isinstance(
                ratio,
                (int, float)
            )
            and ratio > 0)

    def scale(
        self,
        ratio: float):
        if not self.is_valid_ratio(
            ratio):
            raise ValueError("неподходящий коэффициент")

        scaled_ingredients = []
        for ingredient in self.ingredients:
            scaled_ingredients.append(
                Ingredient(
                    ingredient.name,
                    ingredient.quantity*ratio,
                    ingredient.unit
                )
            )
        return Recipe(
            self.title,
            scaled_ingredients
        )

    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):

        recipe_lines = [self.title]
        for ingredient in self.ingredients:
            recipe_lines.append(f"- {ingredient}")
        return "\n".join(recipe_lines)
    




class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(
        self,
        recipe: Recipe,
        portions: float):
        if portions <= 0:
            raise ValueError("необходимо положительно число порций")
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients:
            self._items.append(
                (ingredient, recipe.title))

    def remove_recipe(
        self,
        title: str):
        self._items = [
            item
            for item in self._items
            if item[1] != title]

    def get_list(self):
        ingredients_storage = {}
        for ingredient, _ in self._items:
            key = (ingredient.name,ingredient.unit)
            ingredients_storage[key] = (
                ingredients_storage.get(key, 0)
                + ingredient.quantity)
        result = []
        for (name,unit), quantity in ingredients_storage.items():
            result.append(Ingredient(name,quantity,unit))
        result.sort(
            key=lambda ingredient:
            ingredient.name)
        return result

    def __add__(self,other):
        merged = ShoppingList()
        merged._items = (
            self._items[:] +
            other._items[:])
        return merged