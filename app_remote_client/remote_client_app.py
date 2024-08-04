import os
import webbrowser

from start_remote_client import start_remote_client
from start_local_server import start_local_server, timestamp


HOST = "192.168.206.101" # wlp1s0 IPv4 do servidor primário
PORT = 4400				 # para conexão com servidor primário
LH_PORT = 8000			 # para conexão com browser

TEMP_DIR_PATH = "server_files"
INDEX_PATH = TEMP_DIR_PATH + "/index.html"
STYLE_PATH = TEMP_DIR_PATH + "/style.css"


# estabelece conexão do servidor:
conn, response_data = start_remote_client(HOST, PORT)

# cria servidor web local:
local_server, local_server_ip = start_local_server("localhost", LH_PORT)

if not os.path.exists(TEMP_DIR_PATH):
	# cria diretório temporário para o armazenamento dos
	# arquivos vindos do servidor, caso ainda não exista:
	os.mkdir(TEMP_DIR_PATH)
	print(f"{local_server_ip} - - {timestamp()} >>> localserver: diretório '{TEMP_DIR_PATH}' criado no diretório atual.")

# cria "index.html" na pasta temporária:
index_html = os.open(INDEX_PATH, flags = os.O_WRONLY | os.O_CREAT) # os.O_CREAT: cria arquivo, caso não exista

# armazena bit-stream 'response_data' em "index.html":
os.write(index_html, response_data)

# realiza a requisição de "style.css":
conn.request("GET", "/html_templates/style.css")
http_response = conn.getresponse()
print(f"{local_server_ip} - - {timestamp()} >>> cliente: status da resposta:", http_response.status)
print(f"{local_server_ip} - - {timestamp()} >>> cliente: motivo da resposta:", http_response.reason)

response_data = http_response.read()

# cria "style.css" na pasta temporária:
style_css = os.open(STYLE_PATH, flags = os.O_WRONLY | os.O_CREAT) # os.O_CREAT: cria arquivo, caso não exista

# armazena bit-stream 'response_data' em "style.css":
os.write(style_css, response_data)

# abre arquivo "index.html" no browser padrão do sistema:
BASE_URL = "http://" + local_server_ip + ":" + str(LH_PORT) + "/"
FULL_URL = BASE_URL + INDEX_PATH
try:
	webbrowser.open(FULL_URL, 2) # opens 'FULL_URL' in new tab
except webbrowser.Error as e:
	print(f"{local_server_ip} - - {timestamp()} >>> localserver: conexão com o browser falhou.")
	print(">>> Error: {e}")
	raise

# encerra a conexão com o browser:
#local_server.shutdown()	 # interrompe o loop de processamento de solicitações
							 # encerra a thread
#local_server.server_close() # fecha o socket

# encerra a conexão com o servidor primário:
print(f"{local_server_ip} - - {timestamp()} >>> localserver: encerrando a conexão com o servidor...")
conn.close()

# remove templetes html:
#os.remove(INDEX_PATH)
