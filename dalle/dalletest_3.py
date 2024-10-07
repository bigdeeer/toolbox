# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import base64
import os
from datetime import datetime
import yaml
from openai import AzureOpenAI

api_key = open('apikey3.key', 'r').read()
prompt = open('prompt.yaml', 'r').read()

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://deersw.openai.azure.com/",
    api_key=api_key,
)

size = "1024x1792"
size = "1024x1024"
quality = 'standard'
style = 'vivid'

print("sending request")
b_time = datetime.now()
try:
    result = client.images.generate(
        model="dall-e-3",  # the name of your DALL-E 3 deployment
        prompt=prompt,
        n=1,
        size=size,
        quality=quality,
        style=style,
        response_format='b64_json'
    )
    success = True
except Exception as e:
    print("request rejected")
    print(e)
    exit()
t_time = datetime.now() - b_time
print(f"result received in {t_time}")

try:
    image_data = result.data[0].b64_json
    revised_prompt = result.data[0].revised_prompt
except Exception as e:
    print("invalid result")
    print(result)
    print(e)
    exit()

print("image downloaded")

time_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
os.mkdir(f'output/{time_str}')
output_dir = f'output/{time_str}'

image_bytes = base64.b64decode(image_data)

with open(f'{output_dir}/{time_str}.png', 'wb') as image_file:
    image_file.write(image_bytes)

param = {
    'size': size,
    'quality': quality,
    'style': style
}

with open(f'{output_dir}/params.yaml', 'w') as file:
    yaml.dump(param, file)

with open(f'{output_dir}/prompt.txt', 'w') as file:
    file.write(prompt)

with open(f'{output_dir}/revised_prompt.txt', 'w') as file:
    file.write(revised_prompt)

print("Image saved")
