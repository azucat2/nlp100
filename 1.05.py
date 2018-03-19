#-*- coding: utf-8 -*-

def ngram(data, num):
    res = []
    for i in range(len(data) - num + 1):
        res.append(data[i:i + num])

    return res

str = 'I am an NLPer'
words = str.split(' ')

print('単語', ngram(words, 2))
print('文字', ngram(str, 2))
