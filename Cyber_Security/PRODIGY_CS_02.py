from PIL import Image

import io

def acceptImage ():
    try:
        print("Enter the name of the image: ")
        imageName = input()
        
        fin = open(imageName, 'rb')
        im = fin.read()
        fin.close()
        im = bytearray(im)
        return im, imageName
    except Exception as e:
        print("Error has occured", e)
        return None, None
    
def encrypt (path, im, key):
    for index, values in enumerate(im):
        im[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(im)
    fin.close()
    
def decrypt (path, im, key):
    for index, values in enumerate(im):
        im[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(im)
    fin.close()


im, path = acceptImage()
flag = True
while flag:
    print("Do you want to encrypt or decrypt? (e/d) ", end="")
    action = input()
    action = action.lower()
    if action != "e" and action != "d" or action == "":
        print ("Invalid input! Try again!")
    elif action == "e":
        print ("Enter key: ", end="")
        key = int(input())
        encrypt(path, im, key)
        print("Image encrypted successfully!")
        flag = False
    else:
        print ("Enter key: ", end="")
        key = int(input())
        decrypt(path, im, key)
        print("Image decrypted successfully!")
        flag = False