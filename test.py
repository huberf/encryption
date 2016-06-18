from encryption import *

encrypter = encryption()

while True:
  text = raw_input('Message to encrypt: ')
  encrypt_msg = encrypter.encrypt(text, encrypter.keyGen())
  print encrypt_msg
