# Вызов методов цепочкой

line = "switchport trunk allowed vlan 10,20,30"
words = line.split()
print(words)
vlans_str = words[-1]
print(vlans_str)
vlans = vlans_str.split(",")
print(vlans)

# Предыдущий код можно записать так:
line = "switchport trunk allowed vlan 10,20,30"
vlans = line.split()[-1].split(',')
print(vlans)
