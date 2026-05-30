from HttpRequest import HTTPRequest
import re

class Cors:
    def __init__(self, host="", port="", headers={}, output=""):
        self.host = host
        self.port = port
        self.headers = headers
        self.output = output

    def Scenario1(self):
        req = HTTPRequest(host=self.host, port=self.port, headers={"Origin":"evil.com"})
        res = req.send()
        match0 = re.search(r"Access-Control-Allow-Origin: (.*)", res)
        match1 = re.search(r"Access-Control-Allow-Credentials: true", res)
        if "Access-Control-Allow-Origin: evil.com" in match0.group(0) and "Access-Control-Allow-Credentials: true" in match1.group(0):
            return True
        else:
            return False
    
    def Scenario2(self):
        req = HTTPRequest(host=self.host, port=self.port, headers={"Origin":"null"})
        res = req.send()
        match0 = re.search(r"Access-Control-Allow-Origin: (.*)", res)
        match1 = re.search(r"Access-Control-Allow-Credentials: true", res)
        if "Access-Control-Allow-Origin: null" in match0.group(0) and "Access-Control-Allow-Credentials: true" in match1.group(0):
            return True
        else:
            return False
    
    def Scenario3(self):
        req = HTTPRequest(host=self.host, port=self.port, headers={"Origin":f"subdomain.{self.host}"})
        res = req.send()
        print(res)
        match0 = re.search(r"Access-Control-Allow-Origin: (.*)", res)
        match1 = re.search(r"Access-Control-Allow-Credentials: true", res)
        if f"Access-Control-Allow-Origin: subdomain.{self.host}" in match0.group(0) and "Access-Control-Allow-Credentials: true" in match1.group(0):
            return True
        else:
            return False


    def Result(self):
        if self.Scenario1() or self.Scenario2() or self.Scenario3():
            self.output = f"[+] Vulnerable: CORS Misconfiguration in {self.host}:{self.port}"
        else:
            self.output = f"[x] Not vulnerable: CORS Misconfiguration in {self.host}:{self.port}"
        return self.output 

if __name__ == "__main__":
    analysis = Cors(host="localhost", port=1000)
    res = analysis.Result()
    print(res)

