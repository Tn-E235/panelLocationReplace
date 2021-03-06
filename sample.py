# Python 2.7.16 (default, Mar 25 2021, 18:52:10) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin

import glob
import sys
import os

INPUT_FILE_PATH = './in/'
OUTPUT_FILE_PATH = './out/'
FILES = glob.glob(INPUT_FILE_PATH+'*')
SEARCH_WORD='location'

print('offset_x = ')
OFFSET_X = int(input())
print('offset_y = ')
OFFSET_Y = int(input())

if not os.path.exists(OUTPUT_FILE_PATH):
    os.mkdir(OUTPUT_FILE_PATH)

for f in FILES:
    FILE_R = open(f)
    FILE_NAME = os.path.basename(INPUT_FILE_PATH + f)
    FILE_W = open('./out/'+FILE_NAME, mode='w')

    for l in FILE_R:
        if l.find(';') == 0: 
            FILE_W.write(l)
            continue
        if (l.lower()).find('location') >= 0:
            end = len(l)-1
            com = ""
            if l.find(';')>0:
                end = l.find(';')-1
                com = l[end:]

            x = int(l[l.find('=')+1:l.find(',')]) + OFFSET_X
            y = int(l[l.find(',')+1:end]) + OFFSET_Y
            FILE_W.write(SEARCH_WORD + ' = ' + str(x) + ', ' + str(y) + com + '\n')
        else:
            FILE_W.write(l)

    FILE_R.close()
    FILE_W.close()