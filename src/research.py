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
		docs.append(os.path.join(dirpath, file))


# Créer le vocabulaire de la recherche en ligne de commande
vocab = {}
request = ""
i = 0
for arg in sys.argv :
	if (i != 0) : 
		vocab[arg] = i - 1 # Commence à 0 
		request = request + " " + arg
	i += 1

# Créer matrice des coordonnées (documents / terme)
vectorizer = TfidfVectorizer(input = 'filename', vocabulary = vocab)
M = vectorizer.fit_transform(docs)

#print("Features names")
#print(vectorizer.get_feature_names()) # les termes
#print("Vocabulary")
#print(vectorizer.vocabulary_) #les indices des termes, bon à savoir
#print(M)

#print("#########################################################")

# Créer matrice des coordonnées de la requête
vectorizer2 = TfidfVectorizer(input='content', vocabulary = vocab)
Y = vectorizer2.fit_transform([request])
#print(Y)

def distance_req(d1) : #d1 : indice du doc !!
	numerateur = 0
	somme_carred1 = 0
	somme_carrereq = 0
	for i in range(len(vocab)) : #nb termes
		numerateur += M[d1, i] * Y[0, i]
		somme_carred1 += pow(M[d1,i],2)
		somme_carrereq += pow(Y[0,i],2)
	denumerateur = sqrt(somme_carred1)*sqrt(somme_carrereq)
	if(denumerateur != 0) : return numerateur/denumerateur
	return 0

#print("#########################################################")

print("\nThe documents corresponding to your research are :")

# Filtrer les résultats
dist = {}
results = []
for i in range(len(docs)) : #nb docs
	dist[i] = distance_req(i)
	#print("Distance doc " + str(i) + " to request is :")
	#print(dist[i])
	if(dist[i] > 0.8) : results.append(docs[i])

# Afficher les résultats
for i in range(len(results)) : print(results[i])
print()

