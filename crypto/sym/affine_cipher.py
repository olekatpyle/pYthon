#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import argparse

"""
Affine cipher to encrypt plain text messages. The method does not encrypt sign 
characters. Sign values stay as they are.
"""


signs = ['.', ',', ':', '_', '-', '/', ';', '+', '#', '"', '\'', '%', '&', '(', ')', '?', '!']

def encrypt(key_a: int, key_b: int, msg: str) -> str:

    tmp: list = msg.lower().split()

    def e(ch: str) -> str:
        x = ord(ch) - 97
        y = (key_a * x + key_b) % 26
        return chr(y + 97)

    cipher = '' 
    for s in tmp:
        sub = ''
        for ch in s:
            if ch not in signs:
                ch = e(ch)
            sub = sub + ch
        cipher = cipher + sub + ' '
    
    return cipher



def decrypt(key_a: int, key_b: int, cipher: str):
   
    tmp = cipher.split()

    def inverse(a: int) -> int:
        for i in range(26):
            if a * i % 26 == 1:
                inv: int = i

        return inv

    inv: int = inverse(key_a)

    def d(ch: str):
        y: int = ord(ch) - 97
        x: int = (y - key_b) * inv % 26
        return chr(x + 97)
    
    msg: str = ''
    for s in tmp:
        sub = ''
        for ch in s:
            if ch not in signs:
                ch = d(ch)
            sub = sub + ch
        msg = msg + sub + ' '

    return msg 
         

def main():
    #msg: str = 'falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj!'.lower().split()
    
    parser = argparse.ArgumentParser(prog='Affine Cipher', description="Encryption program using the affine cipher")
    parser.add_argument('-m', '--message', help='The message to encrypt.', dest='msg')
    args: object = parser.parse_args()

    key_a = 7
    key_b = 22
    msg = args.msg
    if msg is None:
        print('You have to provide a message to encrypt!')
        quit()

    print(f'The message you wish to encrypt:\n{msg}')
    cipher: str = encrypt(key_a, key_b, msg)
    print()
    print(f'Your encrypted message: \n{cipher}')
    msg = decrypt(key_a, key_b, cipher)
    print()
    print(f'The decrypted cipher: \n{msg}')


if __name__ == '__main__':
    main()
