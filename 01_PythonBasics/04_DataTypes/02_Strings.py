# Строки

print('Hello World!')

tunnel = """
interface Tunnel0
    ip address 10.10.10.1 255.255.255.0
ip mtu 1416
    ip ospf hello-interval 5
tunnel source FastEthernet1/0
    tunnel protection ipsec profile DMVPN
"""
print(tunnel)

# Суммирование строк
intf = 'interface'
tun = 'Tunnel0'
print(intf + tun)
print(intf + ' ' + tun)
print(intf, tun)
print(intf, tun, end='!\n')

# Умножение строк
print(intf * 5)
print('#' * 50)

# Обращение к символам строки по id
test = 'Test7'
print(test[0])
print(test[2])
print(test[-1])  # Обращение начиная с конца

# Срез строки
str2 = 'Очень длинная строка!'
print(str2[0:21])
print(str2[0:11])
print(str2[7:21])
print(str2[:18])
print(str2[18:])
print(str2[0:-11])
print(str2[-11:])
print(str2[0:10:2])  # С шагом
print(str2[0::2])  # С шагом до конца строки
print(str2[::])
print(str2[::-1])  # Строка в обратном порядке

# Количество символов в строке
print(len(str2))

# Полезные методы для работы со строками
# Метод join
"""
Метод join собирает список строк в одну строку с разделителем,
который указан перед join
"""
vlans = ['10', 'test', '44']
vlans = ' & '.join(vlans)
print(vlans)

# Методы upper, lower, swapcase, capitalize
"""
Методы upper(), lower(), swapcase(), capitalize()
выполняют преобразование регистра строки
"""
string1 = 'FastEthernet'
print(string1)
print(string1.upper())
print(string1.lower())
print(string1.swapcase())

string2 = 'tunnel 0'
print(string2.capitalize())

# Метод count
"""
Метод count() используется для подсчета того,
сколько раз символ или подстрока встречаются в строке
"""
string1 = 'Hello, hello, hello, hello'
print(string1.count('hello'))
print(string1.count('ello'))
print(string1.count('ll'))
print(string1.count('l'))

# Метод find
"""
Методу find() можно передать подстроку или символ,
и он покажет, на какой позиции находится первый символ подстроки
(для первого совпадения)
"""
string1 = 'interface FastEthernet0/1'
print(string1.find('Fast'))
print(string1[string1.find('Fast')::])

# Методы startswith, endswith
"""
Проверка на то, начинается или заканчивается ли строка на определенные символы
(методы startswith(), endswith()):
"""
string1 = 'FastEthernet0/1'
print(string1.startswith('Fast'))
print(string1.startswith('fast'))
print(string1.endswith('0/1'))
print(string1.endswith('0/2'))
"""
Методам startswith() и endswith() можно передавать несколько значений
(обязательно как кортеж)
"""
print("test".startswith(("r", "t")))
print("test".startswith(("r", "a")))
print("rtest".startswith(("r", "a")))
print("rtest".endswith(("r", "a")))
print("rtest".endswith(("r", "t")))

# Метод replace
"""
Замена последовательности символов в строке на другую последовательность
(метод replace()):
"""
string1 = 'FastEthernet0/1'
print(string1)
print(string1.replace('Fast', 'Gigabit'))

# Метод strip
# Убирает спецсимволы
string1 = '\n\tinterface FastEthernet0/1\n'
print(string1)
print(string1.strip())

ad_metric = '[110/1045]'
print(ad_metric)
print(ad_metric.strip('[]'))

# Метод split
"""
Метод split() разбивает строку на части, используя как разделитель какой-то символ
(или символы) и возвращает список строк
"""
string1 = 'switchport trunk allowed vlan 10,20,30,100-200'
commands = string1.split()
print(commands)

vlans = commands[-1].split(',')
print(vlans)

ip = "192.168.100.1"
print(ip.split('.'))

string1 = ' switchport trunk allowed vlan 10,20,30,100-200\n\n'
print(string1.split())

sh_ip_int_br = "FastEthernet0/0            15.0.15.1    YES manual up          up"
print(sh_ip_int_br.split())
print(sh_ip_int_br.split(' '))

# Форматирование строк
# Форматирование строк с методом format
"""
Специальный символ {} указывает, что сюда подставится значение,
которое передается методу format.
При этом каждая пара фигурных скобок обозначает одно место для подстановки.
"""
print("interface FastEthernet0/{}".format(1234567890))
print('{}'.format('qwerty'))
print('{}'.format([12, 55, 98]))

# Вывод результата столбцами
vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']
print('{:>15} {:>15} {:>15}'.format(vlan, mac, intf))
print('{:<15} {:<15} {:<15}'.format(vlan, mac, intf))
print('{:15} {:15} {:15}'.format(vlan, mac, intf))

# Многострочный шаблон
ip_template = '''
IP address:
{}
'''
print(ip_template.format('10.1.1.1'))

# Количество цифр после запятой
print("{:.3f}".format(10.0 / 3))

# Конвертация числа в двоичный формат
print('{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1))

# Конвертация числа в двоичный формат + ширина столбцов
print('{:8b} {:8b} {:8b} {:8b}'.format(192, 100, 1, 1))

# Конвертация числа в двоичный формат + ширина столбцов + дополнение числа нулями, вместо пробелов
print('{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1))

# С указанием емён переменных
print('{ip}/{mask}'.format(mask=24, ip='10.1.1.1'))

# Указание номера аргумента
print('{1}/{0}'.format(24, '10.1.1.1'))
ip_template = '''
IP address:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''  # Без указания номера аргумента
print(ip_template.format(192, 100, 1, 1, 192, 100, 1, 1))
ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''  # С указанием номера аргумента
print(ip_template.format(192, 100, 1, 1))

# Объединение литералов строк
s = 'Test' 'String'
print(s)
s = ('Test'
     'String')
print(s)
message = ('При выполнении команды "{}"'
           'возникла такая ошибка "{}".\n'
           'Исключить эту команду из списка? [y/n]')
print(message)
