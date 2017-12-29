__author__ = 'O.Augusto'
__filename__ = "Expanded_data.py"

import glob
import sys
import random

for i in xrange(10):
	myFile = open("/home/piim/Documentos/RecSys2017/Movielens test1/log.txt").read().split()
	lines = list(myFile)
	random.shuffle(lines)
	out = open('/home/piim/Documentos/RecSys2017/Movielens test1/ExpandedData/log_%s.txt' %(i),'w')
	out.write('\n'.join(lines))
	out.close()

read_files = glob.glob("/home/piim/Documentos/RecSys2017/Movielens test1/ExpandedData/*.txt")

with open("Expanded_Log.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())


