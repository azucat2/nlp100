#-*- coding: utf-8 -*-

import codecs

with codecs.open('hightemp.txt', 'r', 'utf-8') as file:
    lines = file.readlines()

with codecs.open('col1.txt', 'w', 'utf-8') as col1_file,\
        codecs.open('col2.txt', 'w', 'utf-8') as col2_file:
            for line in lines:
                col = line.split('\t')
                col1_file.write(col[0] + '\n')
                col2_file.write(col[1] + '\n')

# 確認
# cut -f1 hightemp.txt
# cut -f2 hightemp.txt
