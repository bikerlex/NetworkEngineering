# Задания

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
print(nat.replace('FastEthernet', 'GigabitEthernet'))
print()

mac = "AAAA:BBBB:CCCC"
print(mac)
mac_list = mac.split(':')
mac = '.'.join(mac_list)
print(mac)
print()

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
print(config)
result = config.split()
print(result[-1].split(','))
print()

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(vlans)
print(sorted(list(set(vlans))))
print()

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
print(command1)
print(command2)
vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))
print(vlans1)
print(vlans2)
print(sorted(list(vlans1.intersection(vlans2))))
print()

ospf_route = "     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
print(ospf_route)
ospf_route = ospf_route.replace('via', '')
ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.split()
print('{:<20} {:<20}'.format('Prefix', ospf_route[0]))
print('{:<20} {:<20}'.format('AD/Metric', ospf_route[1].strip('[]')))
print('{:<20} {:<20}'.format('Next-Hop', ospf_route[2]))
print('{:<20} {:<20}'.format('Last update', ospf_route[3]))
print('{:<20} {:<20}'.format('Outbound Interface', ospf_route[4]))
print()

mac = "AAAA:BBBB:CCCC"
print(mac)
mac_list = mac.strip().split(':')
mac_join = ''.join(mac_list)
mac_hex = int(mac_join, 16)
mac_bin = bin(mac_hex)
mac_final = mac_bin.strip('0b')
print(mac_final)
print()

ip = "192.168.3.1"
print(ip)
ip_list = ip.split('.')
item1 = int(ip_list[0])
item2 = int(ip_list[1])
item3 = int(ip_list[2])
item4 = int(ip_list[3])
print('{:<10} {:<10} {:<10} {:<10}'.format(item1, item2, item3, item4))
print('{:<10b} {:<10b} {:<10b} {:<10b}'.format(item1, item2, item3, item4))
