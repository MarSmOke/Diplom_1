## Unit tests for Stellar Burgers

### Implemented scenarios

Unit tests were created covering the classes `Bun`, `Burger`, `Ingredient`, `Database`

Coverage percentage 100% (report: `htmlcov/index.html`)

### Project structure

- `praktikum` - package containing program code
- `tests` - a package containing tests, divided by class. For example, `bun_test.py`, `burger_test.py`, etc.

###Running autotests

**Installing dependencies**

> `$ pip install -r requirements.txt`

**Running autotests and creating an HTML coverage report**

> `$ pytest --cov=praktikum --cov-report=html`
