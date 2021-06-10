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


for f in FILES:
    FILE_R = open(f)
    FILE_NAME = os.path.basename(INPUT_FILE_PATH + f)
    file_w = open('./out/'+FILE_NAME, mode='w')

    for l in FILE_R:
        if l.find(';') == 0: 
            file_w.write(l[:-1]+'\n')
            continue
        if (l.lower()).find('location') >= 0:
            end = len(l)-1
            com = ""
            if l.find(';')>0:
                end = l.find(';')-1
                com = l[end:]

            x = int(l[l.find('=')+1:l.find(',')]) + OFFSET_X
            y = int(l[l.find(',')+1:end]) + OFFSET_Y
            file_w.write(SEARCH_WORD + ' = ' + str(x) + ', ' + str(y) + com + '\n')
        else:
            file_w.write(l[:-1]+'\n')

    FILE_R.close()
    file_w.close()