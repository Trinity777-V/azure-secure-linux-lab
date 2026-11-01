
from ipaddress import ip_network

vnet = ip_network("10.10.0.0/16")
subred = ip_network("10.10.1.0/24")

direcciones_totales = subred.num_addresses
direcciones_azure = direcciones_totales - 5

print("VNet:", vnet)
print("Subred:", subred)
print("Mascara:", subred.netmask)
print("Direccion de red:", subred.network_address)
print("Ultima direccion:", subred.broadcast_address)
print("IPs totales:", direcciones_totales)
print("IPs disponibles en Azure:", direcciones_azure)
print("Dentro de la VNet:", subred.subnet_of(vnet))
