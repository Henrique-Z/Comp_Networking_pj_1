import start_remote_client

IP = "127.0.1.1"
PORT = 4400
HTTP_REQUEST = \
    """GET / HTTP/1.1
    Host: joseph-81s9
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
    Upgrade-Insecure-Request: 1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Language: en-US,en;q=0.9
    Accept-Encoding: identity
    """

new_client = start_remote_client(IP, PORT, HTTP_REQUEST)
