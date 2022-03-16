# %%
import base64

with open('input.txt', 'rb') as fin, open('output.zip.b64', 'w') as fout:
    base64.encode(fin, fout)
# %%
