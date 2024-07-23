from app_server.start_server import start_server
from app_thread_client.test_server import test_server
from concurrent.futures import ThreadPoolExecutor


PORT = 4400
HTTP_REQUEST = \
	"""GET / HTTP/1.1
	Host: gnu.org
	Connection: keep-alive
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
	Upgrade-Insecure-Requests: 1
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	Accept-Language: en-US,en;q=0.9
	Accept-Encoding: identity"""


# TESTE:
new_server, new_server_ip = start_server(PORT)

thread_pool = ThreadPoolExecutor()
thread_pool.submit(
	test_server(new_server_ip, PORT, HTTP_REQUEST)
)
