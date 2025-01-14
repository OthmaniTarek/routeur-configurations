from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.30.138', 
    'username': 'admin',
    'password': 'admin123',
    'secret': 'admin123',
    'port': 22,
}

conn = ConnectHandler(**cisco_router)

output = conn.send_command('show ip int br')
with open('interfaces.txt', 'w') as fichier:
    fichier.write(output)

commandes = [
    'interface Loopback111',
    'ip address 10.111.111.111 255.255.255.0',
    'no shutdown'
]

conn.enable()
resultat_config = conn.send_config_set(commandes)

with open('resultat_config.txt', 'w') as fichier:
    fichier.write(resultat_config)

conn.disconnect()

print('Configuration terminÃ©e.')
