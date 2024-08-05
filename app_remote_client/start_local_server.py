#import socketserver
#import http.server
import threading
import socket
import time
import os


def timestamp():
	# retorna data e hora local em string formatada:
	return time.strftime(
		"[%d-%m-%Y  %H:%M:%S]",
		time.localtime()
		)


def handle_browser_request(browser_conn, main_conn):
	browser_request = browser_conn.recv(1024).decode()
	#browser_request = browser_conn.recv(1024).decode()
	
	#print("\n\nTYPE:", type(browser_request), "\n")
	print("\n\n", browser_request, "\n")
	
	request_header = browser_request.split()
	print("\n\n", request_header, "\n")
	
	# supondo que requisicoes do browser não são apenas do tipo "GET":
	if request_header[0] is "GET":
		print('ENTROU EM: request_header[0] is "GET"')

	if request_header[0] == "GET":
		REQUESTED_FILE_PATH = request_header[1]		# python walrus operator!?
		if not os.path.exists(REQUESTED_FILE_PATH): # python walrus operator!?
			print(REQUESTED_FILE_PATH.split("/"))
			print(REQUESTED_FILE_PATH.split("/"))
			#FILE_PATH = REQUESTED_FILE_PATH.replace("")
			#/
			# tratar path para requisitar ao servidor primário
			#     ----> em outra variável
			#
			# ignorar favicon request
			REQUESTED_FILE_PATH.pop(0)
			main_conn.request("GET", REQUESTED_FILE_PATH) # !
			http_response = main_conn.getresponse()
			#print(f"{local_server_ip} - - {timestamp()} >>> localserver: status da resposta:", http_response.status) #!
			#print(f"{local_server_ip} - - {timestamp()} >>> localserver: motivo da resposta:", http_response.reason) #!

			response_data = http_response.read() # file bit-stream data

			# cria arquivo requisitado na pasta temporária:
			requested_file = os.open(REQUESTED_FILE_PATH, flags = os.O_WRONLY | os.O_CREAT) # os.O_CREAT: cria arquivo, caso não exista
			
			# armazena bit-stream 'response_data' em 'requested_file':
			os.write(requested_file, response_data)
	else:
		print("INESPERADO")
		return None
	
	pass


def accept_browser_conn(local_server_socket, main_conn):

	#if conn is None:
	#	pass
	# retorna erro!

	while True:
		browser_conn, browser_addr = local_server_socket.accept()
		print(f"[>>> servidor:] Conexão de {browser_addr}")

		# if browser_conn is not None:
		# if browser_addr is not None:
		handle_browser_request(browser_conn, main_conn)
		browser_conn.close()


def start_local_server(port = 8000):

	print("iniciando servidor local...")

	#try:

	ls_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ls_name = socket.gethostname()
	ls_ip = socket.gethostbyname_ex(ls_name)[2][0]
	ls_socket.bind((ls_ip, port)) #local_server_ip
	ls_socket.listen(1)
	print(f"[>>> servidor:] TCP server está ouvindo em {ls_ip}:{port}")
  
	return ls_socket, ls_ip

	""" except Exception:
		if local_server is not None:
			local_server.shutdown()
			local_server.server_close()
		raise """
