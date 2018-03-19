#-*- coding: utf-8 -*-

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str.replace(',', '')
str.replace('.', '')
words = str.split(' ')

for word in words:
    print(len(word), end = '')
