#!/usr/bin/python

import sys, csv, string
import collections

inverted_index = collections.defaultdict(list)

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2: # Something has gone wrong. Skip this line
	        continue

	word = data_mapped[0] #assign the variable word to the first key the intermediate records
	node_id = data_mapped[1]	
	inverted_index[word].append(node_id) #create an index of the words and the node id

for word in inverted_index:
	if word == 'fantastic' or word == 'fantastically':
		print "{0}\t{1}\t{2}".format(word, len(inverted_index[word]), inverted_index[word]) #why are we printing the length

#note.. not listed in descending order.. one is out of place
