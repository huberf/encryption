from encryption import *

encrypter = encryption()

while True:
  text = raw_input('Message to encrypt: ')
  key = encrypter.keyGen()
  encrypt_msg = encrypter.encrypt(text, key)
  print encrypt_msg
  print encrypter.decrypt(encrypt_msg, key)
