import cv2
import numpy as np
from PIL import Image
import random
#it convert data in binary formate
def pubkey(Massege,key):
    temp=[]
    if len(Massege)==len(key):
        return "".join(key)
    elif(len(key)>len(Massege)):
        for i in range(len(Massege)-len(key)):
            temp.append(chr((ord(key[i]+1)-(ord(key[i]))%128)))
            key+= "".join(temp)
    else:
        for i in range(len(Massege)-len(key)):
            temp.append(chr((ord(key[i])+(ord(key[i])+1)%128)))
            key+= "".join(temp)
    return key

def encryption(Massege,key):
    assL=[]
    chiper=[]
    x=1
    for i in range(len(Massege)):
        if(Massege[i]==" "):
            assL.append(ord(" "))
            x+=1
        else:
            assL.append((ord(Massege[i])+ord(key[i])%128)+32)
            x+=1

    for i in assL:
        chiper.append(chr(i))
    return"".join(str(x) for x in chiper)

def decryption(Massege,key):
    assL=[]
    normal=[]
    x=1
    for i in range(len(Massege)):
        if(Massege[i]==" "):
            assL.append(ord(" "))
            normal.append(chr(assL[i]))
        else:
            assL.append((ord(Massege[i])-ord(key[i])-32)%128)
            normal.append(chr(assL[i]))
            x+=1
    return "".join(str(x) for x in normal)

def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p


# hide data in given img

def hidedata(img, data):
    data += "$$"                                   #'$$'--> secrete key
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

 #iterate pixels from image and update pixel values

    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


def encode():
    img_name = input("\nenter image name:")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    message = input("\nenter message:")
    password=input("\nEnter Password:")
    
    key=pubkey(message,password)
    data=encryption(message,key)
    if len(data) == 0:
        raise ValueError("Empty data")
    enc_img = input("\nenter encoded image name:")
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h),Image.ANTIALIAS)
    # optimize with 65% quality
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)


# decoding

def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]


def decode():
    img_name = input("\nEnter Image name : ")
    image = cv2.imread(img_name)
    img=Image.open(img_name,'r')
    password=input("Enter password:")
    cap=random.randint(999,9999)
    print("Capcha=",cap)
    capcha=int(input("Enter the number"))

    if(capcha==cap):
        msg = find_data(image)
        key=pubkey(msg,password)
        return decryption(msg,key)
    else:
        print("Something is wrong!!!")


def stegnography():
    x = 1
    while x != 0:
       print('''\nImage stegnography
       1.encode
       2.decode''')
       u_in = int(input("\n enter your choice:"))
       if u_in == 1:
           encode()
       else:
           ans = decode()
           print("\n your message:\t"+ans)
       x = int(input("\nenter 1 for continue otherwise 0:"))


stegnography()
