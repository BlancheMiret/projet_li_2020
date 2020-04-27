#!/usr/bin/env python3

#import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from math import *

docs=["the house had a tiny little mouse",
      "the cat saw the mouse",
      "the mouse ran away from the house",
      "the cat finally ate the mouse and also it had a big sandwich",
      "the end of the mouse story"
     ]

path = "doctests/"
docs2 = [path + "doc1", path + "doc2", path + "doc3", path + "doc4", path + "doc5"] # 

vocab = {"mouse" : 0, "cat" : 1} # ici entrer les mots de la requête

vectorizer = TfidfVectorizer(input='content', vocabulary = vocab)
X = vectorizer.fit_transform(docs)

v1 = X[0]

#df = pd.DataFrame(v1.T.todense(), index=vectorizer.get_feature_names(), columns =["tfidf"])
#df.sort_values(by=["tfidf"], ascending=False)

print("Features names")
print(vectorizer.get_feature_names()) # les termes
print("Vocaluary")
print(vectorizer.vocabulary_) #les indices des termes, bon à savoir

print("Test 0 : X")
print(X)
print("Test 1: X[0]")
print(v1)
print("Test 2 : X[0,0]")
print(X[0,0])
print("Test3: X.todense()")
print(X.todense())
T = X.todense()
print("Test4 : T[0]")
print(T[0])
print("Test4 : T[0,0]")
print(T[0,0])

#si je veux tfidf pour mot mouse du doc 0
print("Test tfidf mouse doc 0")
i = vectorizer.vocabulary_["mouse"]
print(i)
print(X[0,i])

############################################################################

#remplir tableau de distance de chaque document à la requête
# Donc ajouter la requête en tant que document dans la liste des documents ? 
# Pb : peut pas ajouter et texte ET nom de document...

print("###########")

request = ["mouse cat"]
Y = vectorizer.fit_transform(request)
print("Test Y")
print(Y)

def distance_req(d1) : #d1 : indice du doc !!
	numerateur = 0
	somme_carred1 = 0
	somme_carrereq = 0
	for i in range(len(vocab)) : #nb termes
		numerateur += X[d1, i] * Y[0, i]
		somme_carred1 += pow(X[d1,i],2)
		somme_carrereq += pow(Y[0,i],2)
	#print("numerateur = ", numerateur)
	denumerateur = sqrt(somme_carred1)*sqrt(somme_carrereq)
	#print("denumerateur = ", denumerateur)
	return numerateur/denumerateur

for i in range(len(docs)) : #nb docs
	print("Distance doc " + str(i) + " to request is :")
	print(distance_req(i))














