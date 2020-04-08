#!/usr/bin/env python3

#requirements : wikipedia api
#run $pip3 install wikipedia-api

import wikipediaapi
import sys

if len(sys.argv) < 2 :
	print("usage : ./wiki_copy.py 'page_name1' 'page_name2' ... ")
	exit()


#Create wikipedia object
wiki = wikipediaapi.Wikipedia(
	language = 'fr',
	extract_format = wikipediaapi.ExtractFormat.WIKI)


for i in range(1, len(sys.argv)) :

	#retrieve the page
	page = wiki.page(sys.argv[i] + ' (livre)')
	if not page.exists() :
		page = wiki.page(sys.argv[i])
		if not page.exists() :
			print("%s Wikipedia page does not exist." % sys.argv[i])
			continue

	#format the name for the resulting file
	name = '../documents/'
	c = 0
	for word in sys.argv[i].split() :
		if c == 0 : name += word.lower()
		else : name += '_' + word.lower()
		c += 1

	#write the file
	with open(name, 'w+') as fd :
		fd.write(sys.argv[1] + "\n\n")
		for line in page.text :
			fd.write(line)

	print("The file %s was correctly written." % sys.argv[i])

