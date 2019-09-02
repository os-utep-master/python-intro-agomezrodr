# Python intro
# Adrian Gomez Rodriguez 80625896
#8/31/2019

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

if len(sys.argv) < 3:
    print("To run program, type wordCount.py <inputFileName> <outputFileName>")
    exit()

#declaring variables
inFile = sys.argv[1]
outFile = sys.argv[2]
container = {}   # Words and counts will be stored here.