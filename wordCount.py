# Python intro
# Adrian Gomez Rodriguez 80625896
# 8/31/2019
# Dr. Daniel Cervantes
# Theory of Operating Systems.

import sys  # command line arguments
import re   # regular expression tools
import os   # checking if file exists

#if to check that there are 3 arguments when running programm
if len(sys.argv) < 3:
    print("To run program, type wordCount.py <inputFileName> <outputFileName>")
    exit()

#Declaration
inFile = sys.argv[1]  #declaring input variable
outFile = sys.argv[2]  #declaring output variable
container = {}   # Here is where Words and Counts will be stored.

#check if file is in the path source
if not os.path.isfile(inFile):
    print ("The file %s doesn't exist in the source path" % inFile)
    exit()

#open and read file  (3)
with open(inFile, 'rt') as text:
    for line in text:                       
        line = line.strip()  # .strip() remove all the leading and trailing spaces from a string. (1)
        # print("HERE......") 
        for words in re.split("['\s\t.,-;:=]", line):  #
            # lower() returns a copy of the string in which all case-based characters have been lowercased. (2)
            if words.lower() == "":  
                continue           
                     #    print("CONTINUE......") 
            if words.lower() in container:      
                container[words.lower()] += 1    
                     #    print("Added 1") 
            else:
                container[words.lower()] = 1 
                    #     print("CLOSE") 

                
#sorting and writting in the output file. (4)(5)
output = open(outFile,"w+")
#   print("Openning.....") 
for words, num in sorted(container.items()):
#	outFile.write('%s %s \n' % (word, container[words]) )
    output.write(words + " " + str(num) + "\n")
print 'Output File Ready: %s' % outFile
output.close()

# (1) Refrenced: https://www.geeksforgeeks.org/python-string-strip-2/
# (2) Refrenced: https://www.tutorialspoint.com/python/string_lower.htm
# (3) Refrenced: https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
# (4) Refrenced: https://www.guru99.com/reading-and-writing-files-in-python.html
# (5) Refrenced: https://docs.python.org/2/howto/sorting.html