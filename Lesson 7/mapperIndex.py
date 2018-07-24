#!/usr/bin/python


"""
Q: Write a MR program that creates an index of all words that can be found in the body of a forum post and node id in which they can found. 
#Do not parse the HTML. Just split the text on all whitespace as well as the following characters: .,!?:;"()<>{}#$=-/

1. Map words to IP
"""


import sys
import csv
import string


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t') #read in file 
    specials =  '.,!?:;"()<>{}#$=-/' #split the text on all whitespace as well as the following special characters: .,!?:;"()<>{}#$=-/
    trans = string.maketrans(specials,' '*len(specials)) #allows you to do something with the special characters

    for line in reader: #for each line
	if len(line) == 19: #check to see if there are 19 data fields in the line
		body = line[4] #label the body its the fourth field in the set
		node_id = line[0] #node is the first field in the set
		body = body.translate(trans) #applies the trans function to the text body
		words = body.strip().split() #splits the text body into words
		for word in words: #for each word in the body text
			print "{0}\t{1}".format(word.lower(), node_id) #print mapped keys
		
mapper() #run the function        

