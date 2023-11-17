# Écrire une fonction dont le  paramètre est le répertoire où se trouve l’ensemble des fichiers du corpus
# Qui retourne un dictionnaire associant à chaque mot son score IDF.
# Calculer le logarithme de l'inverse de la proportion de documents qui contiennent ce mot .
# Le temps d'execution de la fonction IDF se situe entre 0.0015 et 0.003 secondes. 

from math import log10
from basicsFunctions import list_of_files,file_reader

def create_file_words_dict(directory="./cleaned/"):
    list_files = list_of_files(directory, ".txt")
    file_words = {}
    for file in list_files:
        words_in_file = set(file_reader(file,directory).split())
        file_words[file] = words_in_file
    return file_words

def CheckWordExist(word, file, file_words):
    return word in file_words[file]

def RegroupAllWords(file_words):
    allWords = set()
    for words_in_file in file_words.values():
        allWords.update(words_in_file)
    return allWords


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