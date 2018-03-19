#-*- config: utf-8 -*-

str = ''
str1 = 'パトカー'
str2 = 'タクシー'

for i in range(4):
    str += (str1+str2)[i::4]

print(str)
