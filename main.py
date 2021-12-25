import os
import sys

cases = ["snake_case", "camelCase", "CONSTANT_CASE", "kebab-case"]


def validate_case(value):
    if value not in cases:
        print("Указанный регистр не поддерживается")
        sys.exit()


def to_camel_case(value):
    content = "".join(value.title().split())
    return content[0].lower() + content[1:]


def to_snake_case(value):
    return "_".join(value.lower().split())


def to_constant_case(value):
    return "_".join(value.upper().split())


def to_kebab_case(value):
    return "-".join(value.lower().split())


def convert(value):
    if target_case == cases[0]:
        return to_snake_case(value)
    elif target_case == cases[1]:
        return to_camel_case(value)
    elif target_case == cases[2]:
        return to_constant_case(value)
    elif target_case == cases[3]:
        return to_kebab_case(value)
    else:
        pass


print("Добро пожаловать в конвертер регистров!")
print("Доступные регистры: snake_case, camelCase, CONSTANT_CASE, kebab-case")

target_case = input("Введите желаемый регистр: ").strip()
validate_case(target_case)
file_path = input("Введите путь к файлу или строку, которую нужно конвертировать: ").strip()

if os.path.exists(file_path):
    file = open(file_path, 'r')
    file_data = file.read()
    converted_file_data = convert(file_data)
    converted_file = open(file_path + "converted", "w")
    converted_file.write(converted_file_data)
    file.close()
    converted_file.close()
    print("Файл успешно записан")
else:
    print(convert(file_path))
