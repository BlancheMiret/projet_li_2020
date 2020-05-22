#!/usr/bin/env python3

from search_engine import *
from math import *
import sys

# Récupérer les noms des documents de la BDD 
docs = fetch_docs()
nb_docs = len(docs)

# Créer le vocabulaire de la recherche en ligne de commande
vocab = build_vocabulary(sys.argv)
nb_terms = len(vocab)

#########################################################

Y = create_TF_IDF_matrix(vocab, docs, nb_terms, nb_docs)

#########################################################

# Liste dont les éléments sont de type [id du document, distance à la requête], trié 
results = measure_distances(Y, nb_docs, nb_terms)

print_results(results, docs)
