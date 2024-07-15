# Проверка типов

# Чтобы проверить, состоит ли строка из одних цифр,
# можно использовать метод isdigit:
print('a'.isdigit())
print('a10'.isdigit())
print('10'.isdigit())
print()

# Метод isalpha позволяет проверить, состоит ли строка из одних букв:
print('a'.isalpha())
print('a100'.isalpha())
print('a--'.isalpha())
print('a '.isalpha())
print()

# Метод isalnum позволяет проверить, состоит ли строка из букв или цифр:
print('a'.isalnum())
print('a10'.isalnum())
print('%'.isalnum())
print()

# Функция type возвращает тип объекта:
print(type('string'))
print(type('string') == str)
print(type((1, 2, 3)))
print(type((1, 2, 3)) == tuple)
print(type((1, 2, 3)) == list)
