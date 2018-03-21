#-*- coding: utf-8 -*-

import codecs

with codecs.open('col1.txt', 'r', 'utf-8') as col1_file,\
        codecs.open('col2.txt', 'r', 'utf-8') as col2_file,\
        codecs.open('merge.txt', 'w', 'utf-8') as merge_file:
            cols1 = col1_file.readlines()
            cols2 = col2_file.readlines()

            for col1, col2 in zip(cols1, cols2):
                merge_file.write(col1.strip() + '\t' + col2.strip() + '\n')

# 確認
# paste col1.txt col2.txt
