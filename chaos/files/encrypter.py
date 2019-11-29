import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "new_"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    #IV stands for Initialization Vector.
    #Used to randomize and produce ciphertest's for certain cipher modes.

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk)%16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                    #padding

                outfile.write(encryptor.encrypt(chunk))


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    #SHA256 produces a 16 byte output no matter what password size is.
    return hasher.digest()

def Main():
    
        filename = input("File to encrypt: ")
        password = input("Password: ")
        encrypt(getKey(password),filename)
        print("File has been encrypted!")

if __name__ == '__main__':
    Main()

