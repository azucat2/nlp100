#-*- coding: utf-8 -*-

def ngram(data, num):
    res = []
    for i in range(len(data) - num + 1):
        res.append(data[i:i + num])

    return res

str1 = 'paraparaparadise'
str2 = 'paragraph'

x = ngram(str1, 2)
y = ngram(str2, 2)

x_set = set(x)
y_set = set(y)

print('X', x)
print('Y', y)
print('和集合', x_set | y_set)
print('積集合', x_set & y_set)
print('差集合', x_set - y_set)
print('xに"se"が含まれるか:' + str('se' in x_set))
print('yに"se"が含まれるか:' + str('se' in y_set))
