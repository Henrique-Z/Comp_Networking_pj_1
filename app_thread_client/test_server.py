"""Módulo que implementa função para testar o servidor TCP."""

import socket
import time

def test_server(server_ip, port, http_request):
	"""criar thread para testar o servidor TCP."""

	thread_client_socket = socket.socket(socket.AF_INET, #	   AF_INET: conexão do tipo IPV4
								  socket.SOCK_STREAM	 # SOCK_STREAM: adota o protocolo TCP
								  )

	time.sleep(2) # coloca a thread para dormir por dois segundos enquanto o servidor é iniciado

	thread_client_socket.connect( (server_ip, port) )

	thread_client_socket.send( bytes(http_request, "utf-8") )
	msg = thread_client_socket.recv(4000)
	print(">> client:", msg)

	thread_client_socket.close()
	print(">> cliente:", thread_client_socket)
