# Задание 5.1

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

name_device = input('Введите имя устройства: ').lower()
device = london_co.get(name_device)
parameters = device.keys()
parameters_str = ', '.join(list(parameters))
name_parameter = input('Введите имя параметра ({}): '.format(parameters_str)).lower()
parameter = device.get(name_parameter, 'Такого параметра нет!')
print(parameter)
