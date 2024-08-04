import socketserver
import http.server
import threading
import socket
import time


def timestamp():
	# retorna data e hora local em string formatada:
	return time.strftime(
        "[%d-%m-%Y  %H:%M:%S]",
        time.localtime()
        )

def start_local_server(host = "localhost", port = 8000):

    local_server = None
    print("iniciando servidor local...")

    try:
        handler = http.server.SimpleHTTPRequestHandler
        local_server = socketserver.TCPServer((host, port), handler)

        local_server_ip, port = local_server.server_address
        if local_server_ip == "0.0.0.0":
            local_server_ip = socket.gethostbyname(socket.gethostname())

        print(f"{local_server_ip} - - {timestamp()} >>> localserver: IPv4 do servidor: {local_server_ip}")
        print(f"{local_server_ip} - - {timestamp()} >>> localserver: servindo na porta: {port}")

        # inicia serviço do servidor em nova thread:
        ls_thread = threading.Thread(target = local_server.serve_forever)
        ls_thread.start()
        
        return local_server, local_server_ip

    except Exception:
        if local_server is not None:
            local_server.shutdown()
            local_server.server_close()
        raise
