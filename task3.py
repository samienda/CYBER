from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

with open('pic_original.bmp', 'rb') as file:
    original_data = file.read()

key = b'Sixteen byte key'

cipherecb = AES.new(key, AES.MODE_ECB)
ciphercbc = AES.new(key, AES.MODE_CBC)

padded_data = pad(original_data, AES.block_size)



header = original_data[:55]


with open('encrypted_ecb.bmp', 'wb') as file:
    file.write(header + cipherecb.encrypt(padded_data)[55:])
    
with open('encrypted_cbc.bmp', 'wb') as file:
    file.write(header + ciphercbc.encrypt(padded_data)[55:])



