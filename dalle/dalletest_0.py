# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://deer-openai-api.openai.azure.com/",
    api_key='4b362368471349f89cc5928e99abdf34',
)

result = client.images.generate(
    model="dall-e-2", # the name of your DALL-E 3 deployment
    prompt="give me a cat picture",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)
