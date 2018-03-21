#-*- coding: utf-8 -*-

import argparse
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int)
args = parser.parse_args()

with codecs.open('hightemp.txt', 'r', 'utf-8') as file:
    for i in range(args.n):
        print(file.readline().strip())

# 確認
# head -n10 hightemp.txt
