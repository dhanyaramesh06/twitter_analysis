import string
import operator
import sys
import time
import collections
import numpy

Read_File = "C:/Users/Dhanya/Desktop/SSDI/AsiaCup2018.txt"

#Storing the read file into a Variable - with encoding format - latin-1
with open(Read_File, encoding="latin-1") as De_encode_File1:
    asiacup2018 = De_encode_File1.readlines()

#using the data from the text file saved in asiacup2018 - variable

MaxRetweets = {}

for dat in asiacup2018:
    file2 = dat.split()    
    if file2[0] not in MaxRetweets:
        MaxRetweets[file2[0]] = int(file2[-1])

MaxRetweets
top_People_with_max_retweets = collections.Counter(MaxRetweets).most_common(10)
top_People_with_max_retweets      
outputFile = open(r'C:/Users/Dhanya/Desktop/SSDI/output/Maximum_retweets.txt', 'w', encoding="utf-8")
outputFile.write("The top 10 users who have maximum retweets is as follows: \n",)

for i in range(0, 10):
    outputFile.write(str(i + 1) + ". Username: " + top_People_with_max_retweets[i][0] + " -> Number of Retweets: " + str(top_People_with_max_retweets[i][1]) + "\n\n")
    outputFile.close
