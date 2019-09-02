# Python intro
# Adrian Gomez Rodriguez 80625896
#8/31/2019

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

if len(sys.argv) < 3:
    print("To run program, type wordCount.py <inputFileName> <outputFileName>")
    exit()

inFile = sys.argv[1]  #declaring input variable
outFile = sys.argv[2]  #declaring output variable
container = {}   # Here is where Words and Counts will be stored.

#check if file is in the path source
if not os.path.isfile(inFile):
    print ("The file %s doesn't exist in the source path" % inFile)
    exit()


with open(inFile, 'rt') as text:
    for line in text:                       
        line = line.strip() 
        # print("HERE......") 
        for words in re.split("['\s\t.,-;:=]", line):
            if words.lower() == "":  
                continue           
                     #    print("CONTINUE......") 
            if words.lower() in container:      
                container[words.lower()] += 1    
                     #    print("Added 1") 
            else:
                container[words.lower()] = 1 
                    #     print("CLOSE") 

                
#sorting and writting in the output file.
output = open(outFile,"w+")
#   print("Openning.....") 
for words, num in sorted(container.items()):
#	outFile.write('%s %s \n' % (word, container[words]) )
    output.write(words + " " + str(num) + "\n")
print 'Output File Ready: %s' % outFile
output.close()


# try:
#     print('Openning file: %s - counting words...' % inputFile)
#     f = open(inputFile, 'r')
#     x = f.read()
#     list1 = re.findall(r'\w+', x, flags=re.I)
#     for words in list1:
#         words = words.lower()
#          if word in list2.key():
#             list2[words] +=1
#             else:
#                 list2[words] = 1
#     f.close()
# output = open(outputFile, 'w+')
# for words in sorted(list2):
#     output.write('%s %s \n' % (words, list2[words]))
#     print 'Output file: %s' %outputFile
# except FileNotFoundError:
#     print'Input File does not exist: %s' % inputFile
#     exit() 
