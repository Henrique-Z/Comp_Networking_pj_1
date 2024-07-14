"""Módulo que implementa função para instanciar e iniciar um cliente TCP."""

import socket

def start_remote_client(server_ip, port, http_request):
    """instancia e inicia um cliente TCP."""

    socket_client = socket.socket(socket.AF_INET,    # ...
                                  socket.SOCK_STREAM # ...
                                  )
    print(socket_client)

    tcp_addrs = ( (server_ip, port) )
    socket_client.connect(tcp_addrs)
    socket_client.send( bytes(http_request, "utf-8") )
    msg = socket_client.recv(port)
    print("client msg:", msg)

    socket_client.close()
    print("client:", socket_client)

    return socket_client
