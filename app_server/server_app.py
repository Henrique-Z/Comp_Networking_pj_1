import socketserver
import http.server
#from start_server import start_IPv4_server


HOST = "0.0.0.0"
PORT = 4400
HTTPD = None


# starts server:
#new_server = start_IPv4_server(PORT)
#new_server.close()

try:
	print("[>>> servidor:] iniciando...")

	HANDLER = http.server.SimpleHTTPRequestHandler
	HTTPD = socketserver.TCPServer((HOST, PORT), HANDLER)
	print("[>>> servidor:] servindo na porta:", PORT)

	HTTPD.serve_forever() # ignores the timeout attribute
except Exception as exc:
	if HTTPD is not None:
		HTTPD.shutdown()     # encerra todos os pedidos
		HTTPD.server_close() # fecha o socket que estava "escutando" a porta
	raise
