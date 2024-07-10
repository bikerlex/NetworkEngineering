# Числа

import math

# Сложение/вычитание
print('Сложение/вычитание')
print(1 + 2)
print(1.0 + 2)
print(10 - 4)

# Умножение
print()
print('Умножение')
print(3 * 3)

# Возведение в степень
print()
print('Возведение в степень')
print(2 ** 3)

# Деление
print()
print('Деление')
print(10 / 3)
print(10 / 3.0)

# Округление
print()
print('Округление')
print(round(10 / 3.0, 2))
print(round(10 / 3.0, 4))

# Остаток от деления
print()
print('Остаток от деления')
print(10 % 3)

# Операторы сравнения
print()
print('Операторы сравнения')
print(10 > 3.0)
print(10 < 3)
print(10 == 3)
print(10 == 10)
print(10 <= 10)
print(10.0 == 10)

# Конвертация в int строки
print()
print('Конвертация в int строки')
a = '11'
print(a)
print(int(a))
print(int(a, 2))  # Двоичное число

# Конвертация в int типа float
print()
print('Конвертация в int типа float')
print(int(3.333))
print(int(3.9))

# Двоичное представление числа
print()
print('Двоичное представление числа')
print(bin(8))  # Получается строка
print(bin(255))

# Шестнадцатеричное представление числа
print()
print('Шестнадцатеричное представление числа')
print(hex(10))

# Более сложные математические функции
print()
print('Более сложные математические функции')
print(math.sqrt(9))  # Квадратный корень
print(math.sqrt(10))
print(math.factorial(5))  # Факториал
print(math.pi)
