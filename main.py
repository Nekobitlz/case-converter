import os
import sys

cases = ["snake_case", "camelCase", "CONSTANT_CASE", "kebab-case"]


def validate_case(value):
    if value not in cases:
        print("Указанный регистр не поддерживается")
        sys.exit()


def convert(value):
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
