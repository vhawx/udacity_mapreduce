#!/usr/bin/python

import sys, csv, string

count = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2: # Something has gone wrong. Skip this line
	        continue

	thisKey, thisValue = data_mapped

	#if thisKey == "fantastically":  #if fantastic
	        #print oldKey, "\t", wordCount

	if oldKey and oldKey != thisKey:
		if oldKey == "fantastic": #if fantastic        
			print oldKey, "\t", count #print key and count
        
	oldKey = thisKey #reset the key to newKey if the oldKey and newKey aren't the same
	count = 0 #reset the count to zero if the oldKey and newKey aren't the same

    	oldKey = thisKey #if oldkey and newkey are the same
    	count += 1 #count

if oldKey != None:
    print oldKey, "\t", count

