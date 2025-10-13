import uuid
import requests
import re
from time import sleep
import argparse
import urllib3
import hashlib
import random

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0 Accept: */*'
CONT_TYPE  = "application/x-www-form-urlencoded"
s = str(random.randint(100000, 999999))
HEADERS = { 'User-Agent'  : USER_AGENT,
            'Content-Type': CONT_TYPE,
            'Cookie': hashlib.md5(s.encode()).hexdigest() }
PROXIES = { 'https' : 'http://127.0.0.1:8080' }

def request_url(url: str, payload: str) -> str:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    req = requests.session()
    s = str(random.randint(100000, 999999))
    data = {"username": s, "country": "Algeria%s"%s}
    r = req.post(url, headers=HEADERS, verify=False, proxies=PROXIES, data=data)
    print(r.text)

def main(payload):
    parser = argparse.ArgumentParser("")
    parser.add_argument("-u","--url",  help="Agrega la url", required=True)
    args = parser.parse_args()
    request_url(args.url, payload)

if __name__ == "__main__":
    while True:
        payload = input("Payload: ")
        main(payload)

