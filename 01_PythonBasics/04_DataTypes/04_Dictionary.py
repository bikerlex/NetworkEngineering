# Словарь (Dictionary)
# изменяемый упорядоченный тип данных

# Пример словаря:
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london)
print(london['name'])

# Можно записывать и так:
london = {
    'id': 1,
    'name': 'London',
    'it_vlan': 320,
    'user_vlan': 1010,
    'mngmt_vlan': 99,
    'to_name': None,
    'to_id': None,
    'port': 'G1/0/11'
}
print(london)
print(london['port'])

# Добавление новой пары ключ - значение
london['test'] = 'Test'
print(london)

# В словаре в качестве значения можно использовать словарь:
london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}
print(london_co['r2']['hostname'])

# Функция sorted сортирует ключи словаря по возрастанию
# и возвращает новый список с отсортированными ключами:
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(sorted(london))

# Метод clear позволяет очистить словарь:
london.clear()
print(london)

# Метод copy позволяет создать полную копию словаря
# Если указать, что один словарь равен другому:
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
london2 = london
print(london)
print(london2)
print(id(london))
print(id(london2))
london['vendor'] = 'Juniper'
print(london)
print(london2)
# это ссылки на один и тот же объект

# Поэтому, если нужно сделать копию словаря, надо использовать метод copy():
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
london2 = london.copy()
print(london)
print(london2)
print(id(london))
print(id(london2))
london['vendor'] = 'Juniper'
print(london)
print(london2)

# Метод get запрашивает ключ, и если его нет, вместо ошибки возвращает None.
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london.get('name'))
print(london.get('ios'))
# Метод get() позволяет также указывать другое значение вместо None:
print(london.get('ios', 'Ooops'))

# Метод setdefault ищет ключ, и если его нет,
# вместо ошибки создает ключ со значением None.
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
ios = london.setdefault('ios')
print(ios)
print(london)
# Если ключ есть, setdefault возвращает значение, которое ему соответствует:
print(london.setdefault('name'))
# Второй аргумент позволяет указать, какое значение должно соответствовать ключу:
model = london.setdefault('model', 'Cisco3580')
print(model)
print(london)

# Методы keys, values, items:
# Все три метода возвращают специальные объекты view
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london.keys())
print(london.values())
print(london.items())
# Конвертация view в список
print(list(london.keys()))

# Метод del удаляет ключ и значение:
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print(london)
del london['name']
print(london)

# Метод update позволяет добавлять в словарь содержимое другого словаря:
r1 = {'name': 'London1', 'location': 'London Str'}
print(r1)
r1.update({'vendor': 'Cisco', 'ios': '15.2'})
print(r1)
# Аналогичным образом можно обновить значения:
r1.update({'name': 'london-r1', 'ios': '15.4'})
print(r1)

############################
# Варианты создания словаря
# Словарь можно создать с помощью литерала:
r1 = {'model': '4451', 'ios': '15.4'}
print(r1)

# Конструктор dict позволяет создавать словарь несколькими способами.
# Если в роли ключей используются строки, можно использовать такой вариант создания словаря:
r1 = dict(model='4455', ios='15.8')
print(r1)
# Второй вариант создания словаря с помощью dict:
r1 = dict([('model', '4451'), ('ios', '15.4'), (123, 456)])
print(r1)

# В ситуации, когда надо создать словарь с известными ключами,
# но пока что пустыми значениями (или одинаковыми значениями),
# очень удобен метод fromkeys():
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
r1 = dict.fromkeys(d_keys)
print(r1)
# По умолчанию метод fromkeys подставляет значение None.
# Но можно указывать и свой вариант значения:
router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
models_count = dict.fromkeys(router_models, 0)
print(models_count)
