"""Módulo que implementa função para instanciar e iniciar um servidor TCP."""

import socket


def start_server(port):
	"""instancia e inicia um servidor TCP."""

	# requisita à API do SO uma conexão:
	server_socket = socket.socket(socket.AF_INET,	 #	   AF_INET: conexão do tipo IPV4
								  socket.SOCK_STREAM # SOCK_STREAM: adota o protocolo TCP
								  )
	print("[>>> servidor:] socket TCP instanciado:\n", server_socket, "\n")

	# pega o atributo de nome do objeto 'server_socket':
	server_name = socket.gethostname()
	print("[>>> servidor:] nome:", server_name)

	# pega o atributo de IP do objeto cujo atributo 'name' é 'server_name':
	server_ip = socket.gethostbyname_ex(server_name)
	server_ip = server_ip[2][0]
	print("[>>> servidor:] IP:", server_ip)

	# impõe que o servidor de ip 'server_ip' apenas "escutará" à porta 'port':
	# AF_INET address family:
	server_socket.bind( (server_ip, port) )

	# permite que o servidor aceite conexões:
	server_socket.listen(1)

	return server_socket, server_ip
