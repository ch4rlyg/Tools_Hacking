import socket
import ssl

class HTTPRequest:
    def __init__(self, host="", method="GET", headers={}, port=443, content_type="", path="/", timeout=5, ssl_verify=False):
        self.host = host
        self.timeout = timeout
        self.method = method
        self.path = path
        self.port = port
        self.content_type = content_type
        self.headers = headers
        self.ssl_verify = ssl_verify

    def build_request(self):
        default_headers = {
            "Host": self.host,
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:150.0) Gecko/20100101 Firefox/150.0",
            "Connection": "close"
        }
        if self.method == "GET":
            all_headers = {**default_headers, **self.headers}
            request = f"{self.method} {self.path} HTTP/1.1\r\n"
            for key,value in all_headers.items():
                request += f"{key}: {value}\r\n"
            request += "\r\n"
            return request

    def send(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.host, self.port))
            context = ssl.create_default_context()
            if not self.ssl_verify:
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
            sock = context.wrap_socket(sock, server_hostname=self.host)
            request = self.build_request()
            sock.send(request.encode())

            response_data = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response_data += chunk
            sock.close()
            return response_data.decode('utf-8')
        except socket.timeout:
            print(f"Timeout after {self.timeout} seconds")

#if __name__ == "__main__":
#    req = HTTPRequest(host="localhost", port=1000)
#    res = req.send()
#    print(res)