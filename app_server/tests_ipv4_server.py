import socketserver
import http.server


HOST = "0.0.0.0"
PORT = 4400
HTTPD = None


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
