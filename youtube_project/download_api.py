import pytube
import yt_dlp


proxies = {'https': "socks5://127.0.0.1:4781"}





def download(url):
    yd = yt_dlp.YoutubeDL({'proxy': proxies})
    yd.proxies = proxies
    a = yd.extract_info(url,download=False)

    print(a)


    yt = pytube.YouTube(url, proxies=proxies)
    yt.bypass_age_gate()
    streaming = yt.vid_info['streamingData']
    data = []

    for _item in streaming['formats'] + streaming['adaptiveFormats']:
        res = _item['qualityLabel'] if 'qualityLabel' in _item else ""
        fps = _item['fps'] if 'fps' in _item else 0
        rate_str = _item['averageBitrate'] if 'averageBitrate' in _item else _item['bitrate']
        bitrate= float(rate_str)/8/1024
        codec = _item['mimeType']
        size = round(float(_item['approxDurationMs']) / 1000 * bitrate/1024, 1)
        url = _item['url']

        item = {'res': res,
                'fps': fps,
                'bitrate': int(bitrate),
                'codec': codec,
                'size': size,
                'url': url}

        data.append(item)

    return data
