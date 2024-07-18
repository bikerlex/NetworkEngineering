# Передача аргументов скрипту (argv)

from sys import argv

filename = argv[0]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('filename {}'.format(filename))
print('\n'.join(access_template).format(filename))
