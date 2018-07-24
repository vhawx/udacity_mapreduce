#!/usr/bin/python

import sys

totalHits = 0
oldKey = None

mostPop = None
mostHits = 0

# Count the number of hits for each different file on the Web site

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisTotal = data_mapped

    if oldKey and oldKey != thisKey:
	if totalHits > mostHits:
		mostHits = totalHits
		mostPop = oldKey
		print oldKey,"\t",totalHits
	totalHits = 0

    oldKey = thisKey
    totalHits += 1

if oldKey != None:
	if totalHits > mostHits:
		mostHits = totalHits
		mostPop = oldKey


print "The most popular file is: ",mostPop,"The number of occurrences is: ",float(mostHits+4)
#Print statement outside of the loop
