import json
from urllib import request
from http import HTTPStatus

import dashscope

dashscope.api_key='sk-16435c32fce6449abe78bd13bfad3f64'

task_response = dashscope.audio.asr.Transcription.async_call(
    model='sensevoice-v1',
    file_urls=[
        'https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/sensevoice/rich_text_example_1.wav'],
    language_hints=['en'],)

transcription_response = dashscope.audio.asr.Transcription.wait(
    task=task_response.output.task_id)

if transcription_response.status_code == HTTPStatus.OK:
    for transcription in transcription_response.output['results']:
        url = transcription['transcription_url']
        result = json.loads(request.urlopen(url).read().decode('utf8'))
        print(json.dumps(result, indent=4, ensure_ascii=False))
    print('transcription done!')
else:
    print('Error: ', transcription_response.output.message)