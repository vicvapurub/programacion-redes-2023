'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 06/12/2023
    Laboratorio: 2.2

'''

import netmiko

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host='10.10.20.48',
    port=22,
    username='developer',
    password='C1sco12345'
)

output = sshCli.send_command("show ip int brief")
print ("show ip int brief:\n{}\n".format(output))

'''
config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description int2'
]

#salida = sshCli.send_config_set(config_commands)
#print(salida)


import re

# Salida del comando
output = "show ip int brief:\nInterface              IP-Address      OK? Method Status                Protocol\nGigabitEthernet0/0     192.168.1.1     YES manual up                    up\nLoopback0              10.0.0.1           YES manual up                    up"

# Expresiones regulares para extraer la dirección IP y el nombre de la interfaz
ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
interface_pattern = r"(\S+)"

# Buscar coincidencias en la salida del comando
matches = re.findall(rf"{interface_pattern}\s+{ip_pattern}", output)

# Verificar si se encontraron coincidencias y extraer los valores
if matches:
    for match in matches:
        interface_name, ip_address = match
        # Imprimir los resultados o almacenar en variables según sea necesario
        print("Dirección IP: {}".format(ip_address))
        print("Nombre de la interfaz: {}".format(interface_name))
else:
    print("No se encontraron coincidencias.")
'''
