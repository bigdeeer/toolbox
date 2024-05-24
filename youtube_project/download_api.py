import pytube

proxies = {'https': "socks5://127.0.0.1:4781"}


def download(url):
    yt = pytube.YouTube(url, proxies=proxies)
    yt.bypass_age_gate()
    streaming = yt.vid_info['streamingData']
    title = yt.title
    thumbnail_url = yt.thumbnail_url
    formats = []

    for _item in streaming['formats'] + streaming['adaptiveFormats']:
        res = _item['qualityLabel'] if 'qualityLabel' in _item else ""
        fps = _item['fps'] if 'fps' in _item else 0
        rate_str = _item['averageBitrate'] if 'averageBitrate' in _item else _item['bitrate']
        bitrate = float(rate_str) / 1024
        codec = _item['mimeType']
        size = round(float(_item['approxDurationMs']) / 1000 * bitrate / 1024, 1)
        url = _item['url']

        _, ext = codec.split('/', 1)
        ext, codec = ext.split(';', 1)
        codec = codec.split('"', 1)[1].split('"', 1)[0]

        item = {'res': res,
                'fps': fps,
                'bitrate': int(bitrate),
                'ext':ext,
                'codec': codec,
                'size': size,
                'url': url}

        formats.append(item)
    data = {
        'formats': formats,
        'title': title,
        'thumbnail_url': thumbnail_url
    }

    return data
