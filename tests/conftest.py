import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient


@pytest.fixture
def burger():
    bun = Bun("Regular Bun", 200)
    ingredient_1 = Ingredient("Sauce", "Chili", 100)
    ingredient_2 = Ingredient("Filling", "Cheese", 150)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    return burger

