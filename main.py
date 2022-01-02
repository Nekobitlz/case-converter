import os
import re
import sys

cases = ["snake_case", "camelCase", "CONSTANT_CASE", "kebab-case"]
validation_error = "Указанный регистр не поддерживается"


def validate_case(value):
    if value not in cases:
        print(validation_error)
        sys.exit()


def to_camel_case(value):
    split_symbol = get_split_symbol(value)
    content = "".join(value.title().split(split_symbol))
    return content[0].lower() + content[1:]


def to_snake_case(value):
    if is_camel_case(value):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', value).lower()
    else:
        split_symbol = get_split_symbol(value)
        return "_".join(value.lower().split(split_symbol))


def to_constant_case(value):
    if is_camel_case(value):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', value).upper()
    else:
        split_symbol = get_split_symbol(value)
        return "_".join(value.upper().split(split_symbol))


def to_kebab_case(value):
    if is_camel_case(value):
        return re.sub(r'(?<!^)(?=[A-Z])', '-', value).lower()
    else:
        split_symbol = get_split_symbol(value)
        return "-".join(value.lower().split(split_symbol))


def is_snake_case(value):
    return re.match('(.*?)_([a-zA-Z])', value)


def is_kebab_case(value):
    return re.match('(.*?)-([a-zA-Z])', value)


def is_constant_case(value):
    return re.match('(.*?)_([A-Z])', value)


def is_camel_case(value):
    return not is_constant_case(value) and re.match('(.+?)([A-Z])', value)


def get_split_symbol(value):
    if is_snake_case(value) or is_constant_case(value):
        return "_"
    elif is_kebab_case(value):
        return "-"
    else:
        return " "


def convert(target_case, value):
    if target_case == cases[0]:
        return to_snake_case(value)
    elif target_case == cases[1]:
        return to_camel_case(value)
    elif target_case == cases[2]:
        return to_constant_case(value)
    elif target_case == cases[3]:
        return to_kebab_case(value)
    else:
        return validation_error


if __name__ == "__main__":
    print("Добро пожаловать в конвертер регистров!")
    print("Доступные регистры:", ', '.join(cases))

    case = input("Введите желаемый регистр: ").strip()
    validate_case(case)
    file_path = input("Введите путь к файлу или строку, которую нужно конвертировать: ").strip()

    if os.path.exists(file_path):
        file = open(file_path, 'r')
        file_data = file.read()
        converted_file_data = convert(case, file_data)
        converted_file = open(file_path + "converted", "w")
        converted_file.write(converted_file_data)
        file.close()
        converted_file.close()
        print("Файл успешно записан")
    else:
        print(convert(case, file_path))
