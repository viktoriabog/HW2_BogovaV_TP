import pytest
from recipes import (
    Ingredient,
    Recipe,
    ShoppingList
)
#-------------------------Тесты для класса Ingredient------------------
def test_ingredient_creation():
    ingredient = Ingredient(
        "Мука",
        500,
        "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient(
        "Мука",
        500,
        "г")
    assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_equal():
    first = Ingredient(
        "Соль",
        100,
        "г")
    second = Ingredient(
        "Соль",
        250,
        "г")
    assert first == second

def test_ingredient_not_equal_name():
    first = Ingredient(
        "Соль",
        100,
        "г")
    second = Ingredient(
        "Сахар",
        100,
        "г")
    assert first != second

def test_ingredient_not_equal_unit():
    first = Ingredient(
        "Молоко",
        1,
        "л")
    second = Ingredient(
        "Молоко",
        1,
        "мл")
    assert first != second


#-------------------------Тесты для класса Recipe------------------

def test_recipe_creation():
    ingredients = [
        Ingredient(
            "Мука",
            500,
            "г")
    ]
    recipe = Recipe(
        "Тесто",
        ingredients
    )
    assert recipe.title == "Тесто"
    assert recipe.ingredients == ingredients

def test_add_new_ingredient():
    recipe = Recipe("Салат")
    ingredient = Ingredient(
        "Огурец",
        100,
        "г")
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ingredient

def test_add_existing_ingredient():
    recipe = Recipe("Салат")
    recipe.add_ingredient(
        Ingredient(
            "Огурец",
            100,
            "г")
    )
    recipe.add_ingredient(
        Ingredient(
            "Огурец",
            50,
            "г")
    )
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 150


def test_scale_returns_new_recipe():
    recipe = Recipe("Тесто")
    recipe.add_ingredient(
        Ingredient(
            "Мука",
            500,
            "г")
    )
    scaled_recipe = recipe.scale(2)
    assert scaled_recipe is not recipe

def test_scale_multiplies_quantities():
    recipe = Recipe("Тесто")
    recipe.add_ingredient(
        Ingredient(
            "Мука",
            500,
            "г")
    )
    scaled_recipe = recipe.scale(2)
    assert (
        scaled_recipe.ingredients[0].quantity
        == 1000
    )

def test_scale_invalid_ratio():
    recipe = Recipe("Тесто")
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_recipe_len():
    recipe = Recipe("Салат")
    recipe.add_ingredient(
        Ingredient(
            "Огурец",
            100,
            "г")
    )
    recipe.add_ingredient(
        Ingredient(
            "Помидор",
            150,
            "г")
    )
    recipe.add_ingredient(
        Ingredient(
            "Огурец",
            50,
            "г")
    )
    assert len(recipe) == 2
    