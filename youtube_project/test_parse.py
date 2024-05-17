import pytube
from pprint import pprint




url = 'https://www.youtube.com/watch?v=PLmbeupnGoo'
yt = pytube.YouTube(url, proxies={'https': "socks5://127.0.0.1:4781"})
yt.bypass_age_gate()
streaming = yt.vid_info['streamingData']
data1 = streaming['formats']
data2 = streaming['adaptiveFormats']
data = data1+data2
for item in data:
    pprint(item)

