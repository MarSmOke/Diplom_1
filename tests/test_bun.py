from bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun("Regular Bun", 199)
        assert bun.get_name() == "Regular Bun"

    def test_get_price(self):
        bun = Bun("Regular Bun", 199)
        assert bun.get_price() == 199
