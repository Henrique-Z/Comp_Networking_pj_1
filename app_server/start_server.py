"""Módulo que implementa função para instanciar e iniciar um servidor TCP."""

import socket


def start_IPv4_server(port = 4400):
	"""instancia e inicia um servidor TCP."""

	# request connection to OS API:
	server_socket = socket.socket(socket.AF_INET,	 # IPV4
								  socket.SOCK_STREAM # TCP protocol
								  )
	print("[>>> servidor:] socket TCP instanciado:\n", server_socket, "\n")

	# get 'name' attribute from 'server_socket' obj:
	server_name = socket.gethostname()
	print("[>>> servidor:] nome:", server_name)

	# get 'IP' attribute from 'server_socket' obj:
	server_ip = socket.gethostbyname_ex(server_name)
	server_ip = server_ip[2][0]
	print("[>>> servidor:] IP:", server_ip)

	# enforces that server will only "listen" to 'port':
	server_socket.bind( (server_ip, port) )

	# open server for connections:
	server_socket.listen(1)

	return server_socket, server_ip


#def start_IPv6_server(host = "::", port = 4400):
#	"""instancia e inicia um servidor TCP."""

#	address = (host, port)

	# request connection to OS API:
#	if socket.has_dualstack_ipv6():
#		server_socket = socket.create_server(address,
#											 family = socket.AF_INET6, # IPv6
#											 dualstack_ipv6 = True     # accept both IPv4 and IPv6, if supported by OS
#											 )
#	else:
#		server_socket = socket.create_server(address)

#	print("[>>> servidor:] socket TCP instanciado:\n", server_socket, "\n")

#	server_info = socket.getaddrinfo(host, port)
#	print("[>>> servidor:] info:", server_info)

#	return server_socket
