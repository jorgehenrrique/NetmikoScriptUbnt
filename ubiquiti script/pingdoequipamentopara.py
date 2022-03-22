from netmiko import ConnectHandler

antena = {
    'device_type': 'ubiquiti_edgerouter',
    'host': '192.168.0.1',  # endereco ip
    'port': '22',  # porta
    'username': 'user',  # usuario
    'password': 'senha',  # senha
}

connect = ConnectHandler(**antena)

comand = connect.send_command('ping -c 6 8.8.8.8')  # ping para dns google 6x

print(comand)  # imprime o ping
