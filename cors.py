from HttpRequest import HTTPRequest
import re

class Cors:
    def __init__(self, host="", port="", headers={"Origin":"evil.com"}, vulnerable=False, output=""):
        self.host = host
        self.port = port
        self.headers = headers
        self.vulnerable = vulnerable
        self.output = output

    def Scenario1(self):
        req = HTTPRequest(host=self.host, port=self.port, headers=self.headers)
        res = req.send()
        match0 = re.search(r"Access-Control-Allow-Origin: (.*)", res)
        match1 = re.search(r"Access-Control-Allow-Credentials: true", res)
        if "Access-Control-Allow-Origin: evil.com" in match0.group(0) and "Access-Control-Allow-Credentials: true" in match1.group(0):
            self.vulnerable = True
        else:
            self.vulnerable = False

    def Result(self):
        self.Scenario1()
        if self.vulnerable:
            self.output = f"[+] Vulnerable: CORS Misconfiguration in {self.host}:{self.port}"
        else:
            self.output = f"[x] Not vulnerable: CORS Misconfiguration in {self.host}:{self.port}"
        return self.output 

if __name__ == "__main__":
    analysis = Cors(host="localhost", port=1000)
    res = analysis.Result()
    print(res)

