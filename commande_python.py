from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'ssh -o HostKeyAlgorithms=+ssh-rsa -o PubKeyAcceptedAlgorithms=+ssh-rsa admin@192.168.30.138',
    'username': 'admin',
    'password': 'admin123',
    'secret': 'admin123',
    'port': 22,
}

with open('fichier_commnds.txt', 'r') as file:
    commands = file.readlines()

conn = ConnectHandler(**cisco_router)
conn.enable()
output = conn.send_config_set(commands)
print(output)
conn.disconnect()

print("Configuration terminée.")
