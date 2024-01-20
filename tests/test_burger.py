import pytest
from burger import Burger
from ingredient import Ingredient
from unittest.mock import Mock


class TestBurger:
    @pytest.mark.parametrize("ingredient_count", [1, 2])
    def test_add_ingredient(self, ingredient_count):
        burger = Burger()
        ingredient_mocks = [Mock(spec=Ingredient) for _ in range(ingredient_count)]
        for ingredient_mock in ingredient_mocks:
            burger.add_ingredient(ingredient_mock)
        assert burger.ingredients == ingredient_mocks

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        initial_ingredients = burger.ingredients.copy()
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == initial_ingredients[1] and burger.ingredients[1] == initial_ingredients[0]

    def test_get_price(self, burger):
        assert burger.get_price() == 650

    def test_receipt(self, burger):
        receipt = burger.get_receipt()
        assert "Regular Bun" and "Sauce Chili" and "Filling Cheese" and "Price: 650" in receipt

