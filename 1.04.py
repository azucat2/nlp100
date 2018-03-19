#-*- coding: utf-8 -*-

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = str.split(' ')

num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words_dict = {}
i = 1
for word in words:
    if i in num:
        words_dict[word[:1]] = i
    else:
        words_dict[word[:2]] = i
    i += 1

print (words_dict)
