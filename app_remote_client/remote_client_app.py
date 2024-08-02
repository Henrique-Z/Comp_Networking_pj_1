import webbrowser
import os
from start_remote_client import start_remote_client


HOST = "192.168.39.101" # IP local do host servidor
PORT = 4400				# número da porta TCP


# estabelece conexão do servidor:
conn, response_data = start_remote_client(HOST, PORT)

INDEX_PATH = "index.html" # "local_buffer/index.html"
with open(INDEX_PATH, "w", encoding="utf-8") as index:
	index.write(response_data)

# abre arquivo "index.html" no browser padrão do sistema:
webbrowser.open(f'file://{os.path.abspath(INDEX_PATH)}')

# encerra a conexão com o servidor:
print("[>>> cliente:] encerrando a conexão com o servidor...")
conn.close()

# remove templetes html:
#os.remove(INDEX_PATH)
