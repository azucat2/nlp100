#-*- coding: utf-8 -*-

import re

def cipher(str):
    res = ''
    for char in str:
        if char.islower():
            res += chr(219 - ord(char))
        else:
            res += char

    return res
    

str = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

result = cipher(str)

print('原文:', str)
print('暗号化:', result)
print('復号:', cipher(result))
