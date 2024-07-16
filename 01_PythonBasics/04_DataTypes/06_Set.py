# Множество (Set)
# изменяемый неупорядоченный тип данных
# В множестве всегда содержатся только уникальные элементы.

vlans = [10, 20, 30, 40, 100, 10]
print(vlans)
print(set(vlans))
print()

##########################################
# Полезные методы для работы с множествами
# Метод add() добавляет элемент во множество:
set1 = {10, 20, 30, 40}
print(set1)
set1.add(50)
print(set1)
print()

# Метод discard() позволяет удалять элементы,
# не выдавая ошибку, если элемента в множестве нет:
set1.discard(55)
print(set1)
set1.discard(50)
print(set1)
print()

# Метод clear() очищает множество:
set1.clear()
print(set1)
print()

#########################
# Операции с множествами
# Объединение множеств можно получить с помощью метода union() или оператора |:
vlans1 = {10, 20, 30, 50, 100}
vlans2 = {100, 101, 102, 200}
print(vlans1)
print(vlans2)
print(vlans1.union(vlans2))
print(vlans1 | vlans2)
print()

# Пересечение множеств можно получить с помощью метода intersection() или оператора &:
vlans1 = {10, 20, 30, 50, 100}
vlans2 = {100, 101, 102, 200}
print(vlans1.intersection(vlans2))
print(vlans1 & vlans2)
print()

#############################
# Варианты создания множества

# Нельзя создать пустое множество с помощью литерала (так как в таком случае это будет не
# множество, а словарь):
set1 = {}
print(type(set1))
# Но пустое множество можно создать таким образом:
set2 = set()
print(type(set2))
print()

# Множество из строки:
print(set('long long long long string'))
print()

# Множество из списка:
print(set([10, 20, 30, 10, 10, 30]))
