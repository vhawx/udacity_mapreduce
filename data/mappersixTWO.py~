#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse

for line in sys.stdin:
	data = line.strip()
	firstIndex = data.find("\"")
	lastIndex = data.rfind("\"")
	if (firstIndex > 1 and lastIndex > 1):
		requestString = line[firstIndex+1:lastIndex]
		actualUrl = requestString.split(" ")[1]
		docname = urlparse(actualUrl)
		print "{0}\t{1}".format(docname.path, 1)

