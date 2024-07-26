#from start_server import start_server
import socketserver
import http.server


HOST = "0.0.0.0"
PORT = 4400
HTTPD = None

# starts server:
#new_server, new_server_ip = start_server(PORT)
#new_server.close()

try:
	handler = http.server.SimpleHTTPRequestHandler # método!?
	HTTPD = socketserver.TCPServer((HOST, PORT), handler)
	HTTPD.serve_forever()
except Exception as exc:
	if HTTPD is not None:
		HTTPD.shutdown()     # encerra todos os pedidos
		HTTPD.server_close() # fecha o socket que estava "escutando" a porta
	raise
