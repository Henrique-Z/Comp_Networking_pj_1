"""Módulo que implementa função para instanciar e iniciar um servidor TCP."""

import socket


def start_server(port):
	"""instancia e inicia um servidor TCP."""

	# requisita à API do SO uma conexão:
	socket_server = socket.socket(socket.AF_INET,	 #	   AF_INET: conexão do tipo IPV4
								  socket.SOCK_STREAM # SOCK_STREAM: adota o protocolo TCP
								  )
	print(socket_server)

	# pega o atributo de nome do objeto 'socket_server':
	server_name = socket.gethostname()
	print("Nome do servidor: ", server_name)

	# pega o atributo de IP do objeto cujo atributo 'name' é 'server_name':
	server_ip = socket.gethostbyname_ex(server_name)
	server_ip = server_ip[2][0]
	print("IP do servidor: ", server_ip)

	# impõe que o servidor de ip 'server_ip' apenas "escutará" à porta 'port':
	# AF_INET address family:
	socket_server.bind( (server_ip, port) )

	return socket_server
