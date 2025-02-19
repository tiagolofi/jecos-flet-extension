import base64
import os

# Gera um token de 128 bits (16 bytes)
token = os.urandom(16)

# Codifica o token em base64
token_base64 = base64.b64encode(token).decode('utf-8')

print(token_base64)