#!/usr/bin/env python3

#Étapes :
# - Récupérer mots clés de la recherche passée en ligne de commande
# - Créer matrice des coordonnées (documents + requête / termes)
# - Créer tableau des distances (requête / documents)
# - Choisir quels documents correspondent à la recherche et afficher leur nom

from sklearn.feature_extraction.text import TfidfVectorizer
from math import *
import sys
import os

# Récupérer la liste des noms des documents de la base de données :
docs = []
path = os.path.join(os.path.abspath(os.getcwd()), "../bdd_utf8") # pour travailler en chemin absolu
for dirpath, dirnames, filenames in os.walk(path) :
	for file in filenames : 
		print(os.path.join(dirpath, file))
		docs.append(os.path.join(dirpath, file))


# Créer le vocabulaire de la recherche en ligne de commande
vocab = {}
i = -1
for arg in sys.argv :
	if (i != -1) : vocab[arg] = i # Commence à 0 
	i += 1

# Créer matrice des coordonnées (documents / terme)
vectorizer = TfidfVectorizer(input='filename', vocabulary = vocab)
M = vectorizer.fit_transform(docs)

print("Features names")
print(vectorizer.get_feature_names()) # les termes
print("Vocaluary")
print(vectorizer.vocabulary_) #les indices des termes, bon à savoir