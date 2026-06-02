import pytest
from recipes import Ingredient

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

