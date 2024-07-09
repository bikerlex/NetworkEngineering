# Синтаксис Python

a = 10
b = 5

if a > b:
    print('A больше B')
    print(a - b)
else:
    print('B больше или равно A')
print('Конец!')


def openfile(filename):
    print('Чтение файла', filename)
    with open(filename) as f:
        print('Готово')
        return f.read()
