#!/usr/bin/python

import sys

'''
Find average sale per day. Intermediate data is day, sale. 
'''

oldKey = None
salesTotal = 0.0
dayCount = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2: 
	        continue
	
	thisKey, sale = data_mapped # or can do thisKey = data[0] ; sale = data[1] 
		
	if oldKey and oldKey != thisKey: # if this is the last record for a specific key; total the results
		salesAvgperDay = salesTotal / dayCount	        
		print oldKey, "\t", salesAvgperDay #print the output. Now that we're finished with that key....
	        oldKey = thisKey #set the oldKey to the newKey
		salesMean = 0 #reset salesMean to zero 
		dayCount = 0 #reset dayCount to zero

	oldKey = thisKey # running total for keys that are the same
	salesTotal += float(sale) # calculate the salesTotal
	dayCount += 1 # calculate the salesTotal

if oldKey != None: #I still dont understand this
	salesAvgperDay = salesTotal / dayCount # find average
	print oldKey, "\t", salesAvgperDay #print average

