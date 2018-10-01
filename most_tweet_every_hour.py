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

mosttweethour = {}

for dat in asiacup2018:
    file2 = dat.split()
    file3 = file2[1].split(":")   #checking the time variable from each line
    Time = file2[0] + " " + file2[1] 
    if Time in mosttweethour:
        mosttweethour[Time] += 1
    else:
        mosttweethour[Time] = 1

mosttweethour = sorted(mosttweethour.items(), key=operator.itemgetter(1), reverse=True)
#mosttweet

mosttweethour2 = {}

totalpostbyuser = 0
for dat in mosttweethour:
    totalpostbyuser += 1
    if (dat[0].split()[1]) in mosttweethour2:
        mosttweethour2[dat[0].split()[1]] += 1
    else:
        mosttweethour2[dat[0].split()[1]] = 1

mosttweethour2 = sorted(mosttweethour2.items(), key=operator.itemgetter(1))
#print(mosttweethour2)

totalEntriesToPrint = 10 * len(mosttweethour2)
outputFile = open(r'C:/Users/Dhanya/Desktop/SSDI/output/Most_tweet_every_hour.txt', 'w',
                  encoding='utf-8')

for x in range(0, len(mosttweethour2)):
    Search = 10
    for dat in mosttweethour:
        if Search == 0:
            break
        if dat[0].split()[1] == mosttweethour2[x][0]:
            outputFile.write("Username: " + dat[0].split()[0] + "\n Hour: " + mosttweethour2[x][0] + "\n")
            Search -= 1
            outputFile.close
