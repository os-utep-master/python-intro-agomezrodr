# Python intro
# Adrian Gomez Rodriguez 80625896
#8/31/2019

import sys # command line arguments
import re  # regular expression tools
import os  # checking if file exists

if len (sys.argv) <3:
    print 'Exced number of arguments'
    print 'Done wordCount.py <inputFile> <outputFile>'
    exit()

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    list1 = {}
    list2 = {}

try:
    print('Openning file: %s - counting words...' % inputFile)
    f = open(inputFile, 'r')
    x = f.read()
    list1 = re.findall(r'\w+', x, flags=re.I)
    for words in list1:
        words = words.lower()

        if word in list2.key():
            list2[words] +=1
            else:
                list2[words] = 1
    f.close()
output = open(outputFile, 'w+')
for words in sorted(list2):
    output.write('%s %s \n' % (words, list2[words]))
    print 'Output file: %s' %outputFile
except FileNotFoundError:
    print'Input File does not exist: %s' % inputFile
    exit()