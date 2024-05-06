import hashlib
import os

blobpath = "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
cache_key = hashlib.sha1(blobpath.encode()).hexdigest()
print(cache_key)


tiktoken_cache_dir = "util/cl100k_base.tiktoken"
os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir

# get the file in 'tik_cache' folder there is only one

# validate
assert os.path.exists(os.path.join(tiktoken_cache_dir, cache_key))
