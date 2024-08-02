import http.client


def start_remote_client(host = None, port = 4400):

	if host is None:
		raise TypeError

	conn = http.client.HTTPConnection(host, port)

	# estabelece os parâmetros necessários para estabelecer o `request`:
	conn.request("GET", "/html_templates/index.html")

	# encaminha o `request` e receber a `response`:
	http_response = conn.getresponse() # variável do tipo `HTTPResponse`
	print("[>>> cliente:] status da resposta:", http_response.status)
	print("[>>> cliente:] reason da resposta:", http_response.reason)

	response_data = http_response.read().decode()
	print("[>>> cliente:] dados na resposta:", response_data)

	response_headers = http_response.getheaders()
	if response_headers:
		print("[>>> cliente:] headers da resposta:\n\t",
			  response_headers[0][0], ":",
			  response_headers[0][1]
			  )

	return conn, response_data
