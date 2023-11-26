# Écrire une fonction dont le  paramètre est le répertoire où se trouve l’ensemble des fichiers du corpus
# Qui retourne un dictionnaire associant à chaque mot son score IDF.
# Calculer le logarithme de l'inverse de la proportion de documents qui contiennent ce mot .
# Le temps d'execution de la fonction IDF se situe entre 0.0015 et 0.003 secondes. 

from math import log10
from basicsFunctions import list_of_files,file_reader

"""
    Fonction qui retourne un dictionnaire { fichier : set(mots dans ce fichier}.
    :param: répertoire des fichiers textes nettoyés
    :return: dictionnaire dont la clé est le ficheir et la valeur de cette clé est un set de tous les mots contenant dans ce fichier
    :rtype: dictionnaire
    """
def create_file_words_dict(directory="./cleaned/"):
    list_files = list_of_files(directory, ".txt")
    file_words = {}
    for file in list_files:
        words_in_file = set(file_reader(file,directory).split())
        file_words[file] = words_in_file
    return file_words

"""
    Fonction qui retourne vrai si le mot existe ou faux si non , dans un fichier, en parcourant le dictionnaire d ela fonction precedente
    :param: le mot qu'on souhaite verifier son existence , le fichier , le dictionnaire files_words
    :return: Vrai si le mot existe , Faux si non 
    :rtype: Booléen
    """
def CheckWordExist(word, file, file_words):
    return word in file_words[file]

"""
    Fonction qui retourne un set qui contient tous les mots de tous les fichiers
    :param: le dictionnaire file_words
    :return: set de tous les mots de tous les fichiers 
    :rtype: set
    """
def RegroupAllWords(file_words):
    allWords = set()
    for words_in_file in file_words.values():
        allWords.update(words_in_file)
    return allWords

"""
    Fonction qui retourne un dictionnaire {mot : score IDF}
    :param: répertoire des fichiers textes nettoyés
    :return: dictionnaire dont les clés sont tous les mots dans tous les fichiers et la valeur de chaque clé est le score IDF 
    :rtype: dictionnaire 
    """
def CalculateIDF(directory="./cleaned/"):
    file_words=create_file_words_dict(directory)
    list_files = list_of_files(directory, ".txt")
    allWords = RegroupAllWords(file_words)
    nb_IDF_words = {}
    for ele in allWords:
        nb_word_existence = 0
        for file in list_files:
            if CheckWordExist(ele, file,file_words):
                nb_word_existence += 1
        nb_IDF_words[ele] = log10(((len(list_files)) / (nb_word_existence)))
    return nb_IDF_words