import http.client


HOST = "192.168.0.108" # IP local do host servidor
PORT = 4400			   # número da porta TCP


conn = http.client.HTTPConnection(HOST, PORT)

# estabelece os parâmetros necessários para estabelecer o `request`:
conn.request("GET", "html_templates/index.html")

# encaminha o `request` e receber a `response`:
http_response = conn.getresponse() # variável do tipo `HTTPResponse`
print("[>>> cliente:] status da resposta:", http_response.status)
print("[>>> cliente:] reason da resposta:", http_response.reason)

response_data = http_response.read().decode()
print("[>>> cliente:] dados na resposta:", response_data)

response_headers = http_response.getheaders()
print("[>>> cliente:] headers da resposta:\n\t",
	  response_headers[0][0], ":",
	  response_headers[0][1]
	  )

# encerra a conexão com o servidor:
print("[>>> cliente:] encerrando a conexão com o servidor...")
conn.close()
