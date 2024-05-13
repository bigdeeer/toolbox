from pytube import request
from pytube.helpers import install_proxy

url = 'https://www.youtube.com/watch?v=PLmbeupnGoo'

endpoint = 'https://www.youtube.com/youtubei/v1/player'
method = 'POST'
headers = {'Content-Type': 'application/json', 'User-Agent': 'com.google.android.apps.youtube.music/'}

data  = {'context': {'client': {'androidSdkVersion': 30, 'clientName': 'ANDROID_MUSIC', 'clientVersion': '5.16.51'}}}
proxies={'https': "socks5://127.0.0.1:4781"}
install_proxy(proxies)
response = request._execute_request(endpoint, method, headers, data)
print(response)
