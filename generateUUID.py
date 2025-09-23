import uuid
import requests
import re
from time import sleep
import argparse
import urllib3

HEADERS = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0 Accept: */*' }
PROXIES = { 'https' : 'http://127.0.0.1:8080' }
EXP_REG = re.compile(r"[0-9a-zA-Z]{8}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{12}")

def generate_uuid() -> str:
    return uuid.uuid4()

def modify_url(url: str) -> str:
    return EXP_REG.sub(lambda _: str(generate_uuid()), url)

def request_url(url: str) -> str:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    req = requests.session()
    url = modify_url(url)
    r = req.get(url, headers=HEADERS, verify=False, proxies=PROXIES)
    print(r.text)

def main():
    parser = argparse.ArgumentParser("")
    parser.add_argument("-u","--url",  help="Agrega la url", required=True)
    args = parser.parse_args()
    request_url(args.url)

if __name__ == "__main__":
    while True:
        main()