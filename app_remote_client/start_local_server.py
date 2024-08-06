#import socketserver
#import http.server
import threading
import socket
import time
import os


def timestamp():
	# retorna data e hora local em string formatada:
	return time.strftime( "[%d-%m-%Y  %H:%M:%S]", time.localtime() )


def handle_browser_request(browser_conn, main_conn):
	browser_request = browser_conn.recv(1024).decode()
	print(">>> localhost: BROWSER REQUEST:", browser_request, "\n")

	request_header = browser_request.split()
	print(">>> localhost: REQUEST HEADER:", request_header, "\n")

	# supondo que requisições do browser não são apenas do tipo "GET":
	if request_header[0] == "GET":
		requested_file_path = request_header[1] # msm path no servidor primário
		# python walrus operator!?

		if not os.path.exists(requested_file_path): # python walrus operator!?
			# ignorar favicon request !

			#FILE_PATH = requested_file_path.replace("")


			main_conn.request("GET", requested_file_path)
			http_response = main_conn.getresponse()
			#print(f"{local_server_ip} - - {timestamp()} >>> localserver: status da resposta:", http_response.status) #!
			#print(f"{local_server_ip} - - {timestamp()} >>> localserver: motivo da resposta:", http_response.reason) #!

			response_data = http_response.read() # file bit-stream data

			if http_response.reason == "404": # not found
				reponse_to_browser = "HTTP/1.1 404 Not Found"
				browser_conn.sendall(reponse_to_browser.encode())
				return browser_conn

			# cria arquivo requisitado na pasta temporária:
			elif http_response.reason == "200": # OK
				if os.name == "nt": # Windows
					nt_path = requested_file_path.replace("/", "\\")
					nt_path = nt_path[1:]
					requested_file = os.open(nt_path, flags = os.O_WRONLY | os.O_CREAT) # os.O_CREAT: cria arquivo, caso não exista

					# armazena bit-stream 'response_data' em 'requested_file':
					os.write(requested_file, response_data)

				elif os.name == "posix": # likely GNU/Linux
					requested_file = os.open(requested_file_path, flags = os.O_WRONLY | os.O_CREAT) # os.O_CREAT: cria arquivo, caso não exista					

					# armazena bit-stream 'response_data' em 'requested_file':
					os.write(requested_file, response_data)

			HTTP_REPONSE = """\
			HTTP/1.1 200 OK\r
			Content-Type: text/html\r
			Content-Length: 44\r
			\r
			"""
			HTTP_REPONSE = HTTP_REPONSE + str(response_data)
			browser_conn.sendall(HTTP_REPONSE.encode())


	else:
		print("METHOD:", request_header[0])
		return None


def accept_browser_conn(local_server_socket, main_conn):

	#if conn is None:
	#	pass
	# retorna erro!

	while True:
		browser_conn, browser_addr = local_server_socket.accept()
		print(f"[>>> servidor:] Conexão de {browser_addr}")

		# if browser_conn is not None:
		# if browser_addr is not None:
		browser_conn = handle_browser_request(browser_conn, main_conn)
		browser_conn.close()


def start_local_server(port = 8000):

	print("iniciando servidor local...")

	try:
		local_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#local_server_name = socket.gethostname()
		#local_server_ip = socket.gethostbyname_ex(local_server_name)
		#local_server_ip = local_server_name[2][0]
		#print("local_server_ip:", local_server_ip)

		local_server_socket.bind( ("0.0.0.0", port) )
		local_server_socket.listen(1)

		#print(f"{local_server_ip} - - {timestamp()} >>> localhost: IPv4 do servidor: {local_server_ip}")
		print(f"127.0.1.1 - - {timestamp()} >>> localhost: servindo na porta {port}")

		return local_server_socket#, local_server_ip

	except Exception:
		if local_server_socket:
			local_server_socket.server_close()

		raise
