#-*- coding: utf-8 -*-

import argparse
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int)
args = parser.parse_args()

with codecs.open('hightemp.txt', 'r', 'utf-8') as file:
    lines = file.readlines()
    for line in lines[-args.n:]:
        print(line.strip())

# 確認
# tail -n10 hightemp.txt
