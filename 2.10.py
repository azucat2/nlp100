#-*- coding: utf-8 -*-

import codecs

with codecs.open('hightemp.txt', 'r', 'utf-8') as file:
    lines = sum(1 for line in file)

print(str(lines))

# 確認
# wc -l
# 24 hightemp.txt
