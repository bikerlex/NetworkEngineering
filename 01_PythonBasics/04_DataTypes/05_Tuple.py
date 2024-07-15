# Кортеж (Tuple)
# неизменяемый упорядоченный тип данных

# Создать пустой кортеж:
tuple1 = tuple()
print(tuple1)

# Кортеж из одного элемента (обратите внимание на запятую):
tuple2 = ('password',)
print(tuple2)

# Кортеж из списка:
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
print(list_keys)
tuple_keys = tuple(list_keys)
print(tuple_keys)

# К объектам в кортеже можно обращаться, как и к объектам списка, по порядковому номеру:
print(tuple_keys[0])

# Но так как кортеж неизменяем, присвоить новое значение нельзя:
# tuple_keys[1] = 'test'

# Функция sorted сортирует элементы кортежа по возрастанию и возвращает новый список с
# отсортированными элементами:
tuple_keys = ('hostname', 'location', 'vendor', 'model', 'ios', 'ip')
print(tuple_keys)
print(sorted(tuple_keys))
