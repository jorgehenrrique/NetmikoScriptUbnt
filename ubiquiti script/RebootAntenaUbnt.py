from netmiko import ConnectHandler

antena = {
	'device_type': 'ubiquiti_edgerouter',
	'host': '192.168.0.1',  # ip do equipamento
	'port': '22',  # porta
	'username': 'user',  # usuario
	'password': 'senha',  # senha
}

connect = ConnectHandler(**antena)

comand1 = connect.send_command("reboot system")  # comando de reboot, ou qualquer outro
