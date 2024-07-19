# Задание 5.2

address = input('Введите ip адрес и маску сети: ')

network, mask = address.split('/')

ip_list = network.split('.')
ip1, ip2, ip3, ip4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3])
]

mask = int(mask)
mask_bin = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(mask_bin[0:8], 2),
    int(mask_bin[8:16], 2),
    int(mask_bin[16:24], 2),
    int(mask_bin[24:32], 2)
]

network_template = """
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}"""

mask_template = """
Mask:
/{0:}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}"""

print(network_template.format(ip1, ip2, ip3, ip4))
print(mask_template.format(mask, m1, m2, m3, m4))
