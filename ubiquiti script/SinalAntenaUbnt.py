from netmiko import ConnectHandler

antena = {
	'device_type': 'ubiquiti_edgerouter',
	'host': '192.168.0.1',  # ip do equipamento
	'port': '22',  # porta
	'username': 'user',  # usuario
	'password': 'senha',  # senha
}

connect = ConnectHandler(**antena)

comand1 = connect.send_command("cd /")  # ir para pasta padrao
comand2 = connect.send_command("./usr/www/signal.cgi")  # obter sinal do equipamento a partir do diretorio

print(comand2)  # imprimir sinal