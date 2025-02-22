# Список (List)
# изменяемый упорядоченный тип данных

# Примеры списков:
list1 = [10, 20, 30]
list2 = ['one', 'dog', 'seven']
list3 = [1, 20, 4.0, 'word']
print(list1)
print(list2)
print(list3)

# Создание списка с помощью литерала:
vlans = [10, 20, 30, 50]
print(vlans)

# Создание списка с помощью функции list():
list4 = list('router')
print(list4)
print(list4[2])  # обращение к элементу списа по номеру
print(list4[-2])  # обращение к элементу списа по номеру начиная с конца
print(list4[0:3])  # срез списка
print(list4[1::2])  # срез списка с шагом

# Перевернуть список наоборот можно и с помощью метода reverse():
list4.reverse()
print(list4)

# Так как списки изменяемые, элементы списка можно менять:
list4[0] = 'test'
print(list4)

# Можно создавать и список списков.
# И, как и в обычном списке, можно обращаться к элементам во вложенных списках:
interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
print(interfaces[0])
print(interfaces[0][0])
print(interfaces[2][1])

# Функция len возвращает количество элементов в списке:
print(len(list4))

# Функция sorted сортирует элементы списка по возрастанию и возвращает новый список с
# отсортированными элементами:
print(sorted(list4))

########################################
# Полезные методы для работы со списками
# Метод append добавляет в конец списка указанный элемент:
list4.append('last')
print(list4)

# Объединение списков методом extend:
vlans = ['10', '20', '30', '100-200']
vlans2 = ['300', '400', '500']
vlans.extend(vlans2)
print(vlans)

# Суммирование списков:
vlans = ['10', '20', '30', '100-200']
vlans2 = ['300', '400', '500']
result = vlans + vlans2
print(result)

# Метод pop удаляет элемент, который соответствует указанному номеру
# и возвращяет этот элемент
# Без указания номера удаляется последний элемент списка.
vlans = ['10', '20', '30', '100-200']
print(vlans)
item = vlans.pop(2)
print(item)
print(vlans)

# Метод remove удаляет указанный элемен не возвращая удалённый элемент
vlans = ['10', '20', '30', '100-200']
vlans.remove('20')
print(vlans)

# Метод index используется для того, чтобы проверить,
# под каким номером в списке хранится элемент:
vlans = ['10', '20', '30', '100-200']
print(vlans.index('100-200'))

# Метод insert позволяет вставить элемент на определенное место в списке:
vlans = ['10', '20', '30', '100-200']
vlans.insert(1, '15')
print(vlans)

# Метод sort сортирует список на месте:
vlans = [1, 50, 10, 15]
vlans.sort()
print(vlans)
