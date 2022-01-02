import main


def test_convert_case_error():
    assert main.convert("error case", "error case") == main.validation_error


def test_convert_camel_case():
    assert main.convert("camelCase", "my own camel case") == "myOwnCamelCase"
    assert main.convert("camelCase", "camel") == "camel"
    assert main.convert("camelCase", "camel case") == "camelCase"


def test_convert_snake_case():
    assert main.convert("snake_case", "my own snake case") == "my_own_snake_case"
    assert main.convert("snake_case", "snake") == "snake"
    assert main.convert("snake_case", "snake case") == "snake_case"


def test_convert_constant_case():
    assert main.convert("CONSTANT_CASE", "my own constant case") == "MY_OWN_CONSTANT_CASE"
    assert main.convert("CONSTANT_CASE", "constant") == "CONSTANT"
    assert main.convert("CONSTANT_CASE", "constant case") == "CONSTANT_CASE"


def test_convert_kebab_case():
    assert main.convert("kebab-case", "my own kebab case") == "my-own-kebab-case"
    assert main.convert("kebab-case", "kebab") == "kebab"
    assert main.convert("kebab-case", "kebab case") == "kebab-case"


def test_convert_to_other_case():
    assert main.convert("camelCase", "snake_case") == "snakeCase"
    assert main.convert("camelCase", "CONSTANT_CASE") == "constantCase"
    assert main.convert("camelCase", "kebab-case") == "kebabCase"

    assert main.convert("snake_case", "camelCase") == "camel_case"
    assert main.convert("snake_case", "CONSTANT_CASE") == "constant_case"
    assert main.convert("snake_case", "kebab-case") == "kebab_case"

    assert main.convert("CONSTANT_CASE", "camelCase") == "CAMEL_CASE"
    assert main.convert("CONSTANT_CASE", "snake_case") == "SNAKE_CASE"
    assert main.convert("CONSTANT_CASE", "kebab-case") == "KEBAB_CASE"

    assert main.convert("kebab-case", "camelCase") == "camel-case"
    assert main.convert("kebab-case", "CONSTANT_CASE") == "constant-case"
    assert main.convert("kebab-case", "snake_case") == "snake-case"
