from utils import calculate_occurence_words
from utils import calculate_idf
from utils import list_of_files
from text_organization import string_cleaner

def score_TF_question(string):
    """
    Function that calculate the occurence of words in a string

    Parameters:
        string
    Returns:
        dictionary of word : TF
    """
    TF = calculate_occurence_words(string)
    list_of_words = string_cleaner(string)
    # si mot n'est pas dsans matrice alors non
    for key , val in TF.items():
        TF[key] = val/len(list_of_words)
    return TF
print(score_TF_question("le climat Saraah"))
def dict_score_TFIDF_question (string):
    DictIDF = calculate_idf(directory="./cleaned/",extension=".txt")
    DictTFIDF = score_TF_question(string)
    for key , val in DictTFIDF.items():
        if key in DictIDF :
            DictTFIDF[key]= val * DictIDF[key]
    return DictTFIDF
print(dict_score_TFIDF_question("Le climat Sarah"))

def tfidf_matrix_of ( string ):
    DictTFIDF = dict_score_TFIDF_question(string)
    tfidfTuple = ([],[])
    for key , val in DictTFIDF.items():
        tfidfTuple[0].append(key)
        tfidfTuple[1].append(val)
    tfidfMatrix = []
    for element in tfidfTuple:
        tfidfMatrix.append(element)
    return tfidfMatrix
print(tfidf_matrix_of("Le climat Sarah"))


