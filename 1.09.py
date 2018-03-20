#-*- coding: utf-8 -*-

import random

def typoglycemia(str):
    words = str.split(' ')
    res = []

    for word in words:
        if len(word) > 4:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            res.append(word[:1] + ''.join(chr_list) + word[-1:])
        else:
            res.append(word)

    return ' '.join(res)

str = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

print(str)
print(typoglycemia(str))
