from start_remote_client import start_remote_client


HOST = "192.168.39.1081" # IP local do host servidor
PORT = 4400		 # número da porta TCP


try:
	conn, response_data = start_remote_client(HOST, PORT)
except TypeError as e:
	print("[>>> cliente:] host do servidor não informado")
	raise

# encerra a conexão com o servidor:
print("[>>> cliente:] encerrando a conexão com o servidor...")
conn.close()
