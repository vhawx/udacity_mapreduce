#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("GET /assets/js/the-associates.js HTTP/1.1")
    if len(data) > 1:
        docname = data[1].split(" ")[0]
        print "{0}\t{1}".format(docname, 1)

