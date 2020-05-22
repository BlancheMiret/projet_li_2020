#!/usr/bin/env python3

from sklearn.feature_extraction.text import TfidfVectorizer
from search_engine import *
import sys

# Récupérer la liste des noms des documents de la base de données :
docs = fetch_docs()
nb_docs = len(docs)

# Créer le vocabulaire de la recherche en ligne de commande
vocab = build_vocabulary(sys.argv)
nb_terms = len(vocab)

#########################################################

# Créer matrice des coordonnées (documents / terme)
vectorizer = TfidfVectorizer(input = 'filename', sublinear_tf = True, vocabulary = vocab)
M = vectorizer.fit_transform(docs)

# Créer matrice des coordonnées de la requête
request = build_request(sys.argv)
vectorizer2 = TfidfVectorizer(input='content', vocabulary = vocab)
Y = vectorizer2.fit_transform([request])

#########################################################

# Liste dont les éléments sont de type [id du document, distance à la requête], trié 
results = measure_distances(M, nb_docs, nb_terms, Y[0,0])

# Afficher les résultats
print_results(results, docs)
