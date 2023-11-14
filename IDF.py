# Écrire une fonction dont le  paramètre est le répertoire où se trouve l’ensemble des fichiers du corpus
# Qui retourne un dictionnaire associant à chaque mot son score IDF.
# Calculer le logarithme de l'inverse de la proportion de documents qui contiennent ce mot .
from math import log10
from basicsFunctions import list_of_files

def CheckWordExist(word, file, directory='./cleaned/'):
    with open(directory+file, 'r') as file:
        for line in file:
            for ele in line.split():
                if word==ele:
                    return True
        return False
    
def RegroupAllWords(directory='./cleaned/'):
    list_files=list_of_files(directory,'.txt')
    allWords=set()
    for file in list_files:
        with open(directory+file,'r') as file:
            for line in file:
                for word in line.split():
                    allWords.add(word)
    return allWords

def CalculateIDF(directory='./cleaned/'):
    list_files=list_of_files(directory,'.txt')
    allWords=RegroupAllWords(directory)
    nb_IDF_words={}
    for ele in allWords:
        nb_word_existence=0
        for file in list_files:
            if CheckWordExist(ele,file):
                nb_word_existence+=1
        nb_IDF_words[ele]=log10(((len(list_files))/(nb_word_existence)))
    return nb_IDF_words
