#-*- coding: utf-8 -*-

import codecs

with codecs.open('hightemp.txt', 'r', 'utf-8') as file:
    res = file.read().replace('\t', ' ')

print(res)

# 確認
# sed -e 's/\t/ /g' hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t1 hightemp.txt
