import time
import socketserver
import http.server

from get_IPv4_external_address import get_IPv4_external_address


def get_timestamp():
	# pega data e hora local e retorna em uma string formatada:
	timestamp = time.strftime("[%d-%m-%Y  %H:%M:%S]", time.localtime()) # [%d/%b/%Y %H:%M:%S]
	return timestamp


HOST = "0.0.0.0"
PORT = 4400
INTERFACE_NAME = "wlp1s0"


server = None
print("iniciando servidor...")

try:
	handler = http.server.SimpleHTTPRequestHandler
	server = socketserver.TCPServer((HOST, PORT), handler)

	# pega IPv4 que clientes devem usar para poderem se conectar:
	server_ip = get_IPv4_external_address(INTERFACE_NAME)

	print(f"{server_ip} -- {get_timestamp()} >>> servidor: IPv4 da interface {INTERFACE_NAME}: {server_ip}")
	print(f"{server_ip} -- {get_timestamp()} >>> servidor: servindo na porta {PORT}")

	server.serve_forever() # ignores the timeout attribute

except Exception as e:
	if server is not None:
		server.shutdown()     # encerra todos os pedidos
		server.server_close() # fecha o socket que estava "escutando" a porta
	raise
