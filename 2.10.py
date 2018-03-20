#-*- coding: utf-8 -*-

import subprocess
import codecs

lines = sum(1 for line in codecs.open('hightemp.txt', 'r', 'utf-8'))

print(str(lines))

# 確認
# wc -l
# 24 hightemp.txt
