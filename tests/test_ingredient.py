from ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient("Sauce", "Chili", 150)
        assert ingredient.get_price() == 150

    def test_get_name(self):
        ingredient = Ingredient("Sauce", "Chili", 150)
        assert ingredient.get_name() == "Chili"

    def test_get_type(self):
        ingredient = Ingredient("Sauce", "Chili", 150)
        assert ingredient.get_type() == "Sauce"
