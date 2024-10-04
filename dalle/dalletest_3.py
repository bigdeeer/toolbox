# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os

import requests
import yaml
from openai import AzureOpenAI
import json

# read api from text
api_key = open('apikey3.key', 'r').read()
# load prompt from text
prompt = open('prompt.yaml', 'r').read()

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://deersw.openai.azure.com/",
    api_key=api_key,
)

result = client.images.generate(
    model="dall-e-3",  # the name of your DALL-E 3 deployment
    prompt=prompt,
    n=1,
    # size='1024x1792',
    # style='natural',
    # quality='hd'

)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)
