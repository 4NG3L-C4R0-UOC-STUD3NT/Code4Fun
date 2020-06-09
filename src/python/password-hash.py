import os
import sys
import hashlib 
import random

password_salt = os.urandom(32).hex()
password = '12345'
hash = hashlib.sha512()
hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
password_hash = hash.hexdigest()
print("password: {}".format(password))
print("password salt: {}".format(password_salt))
print("password hash: {}".format(password_hash))
