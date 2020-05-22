from sklearn.feature_extraction.text import CountVectorizer
from math import *
import string
import os


################### CONSTRUCTING DATA ###################

def fetch_docs() :
	docs = []
	path = os.path.join(os.path.abspath(os.getcwd()), "../bdd_utf8") # pour travailler en chemin absolu
	for dirpath, dirnames, filenames in os.walk(path) :
		for file in filenames : 
			if(file != ".DS_Store") : docs.append(os.path.join(dirpath, file))
	return docs

def build_request(args):
	request = ""
	i = 0
	for arg in args :
		if (i != 0) : request = request + " " + arg
		i += 1
	return request

def build_vocabulary(args) :
	vocab = {}
	i = 0
	for arg in args :
		if (i != 0) : 
			arg = arg.lower()
			vocab[arg] = i - 1 # Commence à 0 
		i += 1
	return vocab


####################### DISTANCES #######################

def distance_req(di, nb_terms, M, Y = 1) :
	numerateur = 0
	somme_carred1 = 0
	somme_carrereq = 0
	for i in range(nb_terms) : #nb termes
		numerateur += M[di, i] * Y
		somme_carred1 += pow(M[di,i],2)
		somme_carrereq += pow(Y,2)
	denumerateur = sqrt(somme_carred1)*sqrt(somme_carrereq)
	if(denumerateur != 0) : return numerateur/denumerateur
	return 0

def measure_distances(M, nb_docs, nb_terms, Y = 1) :
	distances = []
	for i in range(nb_docs) : 
		dist = distance_req(i, nb_terms, M, Y)
		if(dist > 0.8) : 
			distances.append([i, dist])
	return quick_sort_dbl(distances)


######################## SORTING ########################

def quick_sort_dbl(T) :
	if len(T) < 2 : return T
	pivot, left, right = partition_dbl(T)
	return quick_sort_dbl(left) + pivot + quick_sort_dbl(right)

def partition_dbl(T) :
	pivot = [elt for elt in T if elt[1] == T[0][1]]
	left  = [elt for elt in T if elt[1] > pivot[0][1]]
	right = [elt for elt in T if elt[1] < pivot[0][1]]
	return pivot, left, right


######################## RESULTS ########################

def format_title(title) :
	title = title.replace("/Users/blanchemiret/Workspace/GitHub/projet_li_2020/src/../bdd_utf8/", "")
	title = title.replace("_", " ")
	return string.capwords(title)

def print_results(results, docs) :
	print("\nThe documents corresponding to your research are :")
	for elt in results : 
		print(format_title(docs[elt[0]]) + " : " + str(elt[1])) 
	print()


######################### MATRIX ########################

def compute_term_frequency(M, nb_terms, nb_docs) :
	TF = []
	for i in range(nb_terms) :
		dwt = 0
		for j in range(nb_docs) :
			if(M[j, i]) != 0 : dwt +=1
		TF.append(dwt)
	return TF

def create_TF_IDF_matrix(vocab, doc_list, nb_terms, nb_docs) :
	vector = CountVectorizer(input = 'filename', vocabulary = vocab)
	X = vector.fit_transform(doc_list)
	TF = compute_term_frequency(X, nb_terms, nb_docs)
	Y = X.todense()
	for i in range(nb_terms) :
		for j in range(nb_docs) :
			Y[j, i] = Y[j, i] * TF[i]
	return Y
