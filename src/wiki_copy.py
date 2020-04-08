#!/usr/bin/env python3

#requirements : wikipedia api
#run $pip3 install wikipedia-api

import wikipediaapi
#import wikipedia
import sys

if len(sys.argv) != 2 :
	print("usage : ./wiki_copy.py page_name")
	exit()


#Create wikipedia object
wiki = wikipediaapi.Wikipedia(
	language = 'fr',
	extract_format = wikipediaapi.ExtractFormat.WIKI)

#wikipedia.set_lang('fr')
#print(wikipedia.suggest('Citadelle'))
#print(wikipedia.summary('La Horde du Contrevent (livre)'))


#retrieve the page
page = wiki.page(sys.argv[1] + ' (livre)')
if not page.exists() :
	print("This Wikipedia page does not exist.")
	exit()


#format the name for the ending file
name = '../documents/'
i = 0
for word in sys.argv[1].split() :
	if i == 0 : name += word.lower()
	else : name += '_' + word
	i += 1


#write the file
with open(name, 'w+') as fd :
	fd.write(sys.argv[1] + "\n\n")
	for line in page.text :
		fd.write(line)

print("The file was correctly written.")

