'''
cryptography using python
AES Algorithm
by amirkho.ir
github.com/amirkho-py/

'''

from os import system
from cryptography.fernet import Fernet


system("clear") # or "cls" to clean the terminal


key = Fernet.generate_key() # generate a symmetric key

message = "Hello".encode() # source data for encrypting
 
f = Fernet(key) # AES algorithm class 

encrypted = f.encrypt(message) # enrypting function

decrypted = f.decrypt(encrypted) # decripting function

# print encrypted source data - key - decrypted data
print("encrypted data:" , encrypted)
print("key:",key)
print("decrypted data:",decrypted.decode())

