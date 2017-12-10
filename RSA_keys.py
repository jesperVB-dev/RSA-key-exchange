import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import os

def CreateKeys():
    random_generator = Random.new().read
    key = key = RSA.generate(2048, os.urandom)
    publickey = key.publickey() 
    #print (key.publickey()).exportKey()
    with open("rsa.pub", "w") as pub_file:
        pub_file.write(publickey.exportKey())
    with open("rsa.pvt", "w") as pvt_file:
        pvt_file.write(key.exportKey())
    return publickey, key

def LoadPubKey():
    with open('rsa.pub', 'r') as pub_file:
        publickey = RSA.importKey(pub_file.read())
        
    return publickey

def LoadPrivKey():
    with open('rsa.pvt', 'r') as pub_file:
        privatekey = RSA.importKey(pub_file.read())
        
    return privatekey

def Encrypt(message, publickey):
    encrypted = publickey.encrypt(message, 2048)
    print 'encrypted message:', encrypted
    return encrypted

def Decrypt(key, encrypted):
    
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted

#CreateKeys()
Encrypted = Encrypt("{insert codes here}", LoadPubKey())
print Decrypt(LoadPrivKey(), Encrypted)
#Codes = '' #i.e Codes = '{"a":"12","b":48,...}'
#print Encrypt(Codes, "") #put the public key i've send you in the second argument

