#!/usr/bin/python

import sys

salesTotal = 0
keyTotal = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data

    #if oldKey and oldKey != thisKey:
        #print oldKey, "\t", salesTotal
        
	#salesTotal = 0

    #oldKey = thisKey
    salesTotal += float(thisSale)
    keyTotal += float(thisKey) 

#if oldKey != None:
print keyTotal, "\t", salesTotal

