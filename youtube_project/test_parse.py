from pprint import pprint
import json
import socket

from urllib import request
from urllib.request import Request, urlopen

url = 'https://www.youtube.com/watch?v=PLmbeupnGoo'

endpoint = 'https://www.youtube.com/youtubei/v1/player'
method = 'POST'
headers = {'Content-Type': 'application/json', 'User-Agent': 'com.google.android.apps.youtube.music/'}

data = {'context': {'client': {'androidSdkVersion': 30, 'clientName': 'ANDROID_MUSIC', 'clientVersion': '5.16.51'}}}
proxies = {'https': "socks5://127.0.0.1:4781"}

proxy_support = request.ProxyHandler(proxies)
opener = request.build_opener(proxy_support)
request.install_opener(opener)

base_headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
base_headers.update(headers)
data = bytes(json.dumps(data), encoding="utf-8")
request = Request(url, headers=base_headers, method=method, data=data)
response = urlopen(request, timeout=1000)  # nosec

pprint(response.read())
