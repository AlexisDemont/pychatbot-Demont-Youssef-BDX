import os
from math import log10

def list_of_files(directory, extension):
    """
    Fonction qui retourne une liste dont les elements sont les noms des fichiers qui se trouve dans repertoire et se terminent par des extensions precis 
    :param: répertoire et extension
    :return: liste des noms des fichiers 
    :rtype: liste
    """
    return [filename for filename in os.listdir(directory) if filename.endswith(extension)]

def clean_folder(directory='./cleaned', extension='txt'):
    """
    Fonction qui retourne vrai lorsque la suppression de tous les fichiers de la liste 'list_of_files' dans le repertoire cleaned et dont l'extension (txt), a été effectuée 
    :param: répertoire des fichiers textes nettoyés, et extension (txt)
    :return: True lorsque la suppression de tous les fichers dans la liste files_name dans le repertoire cleaned (txt)
    :rtype: Booléen
    """
    for name in list_of_files(directory, extension):
        os.remove(directory + name)
    return


def file_reader(file,directory):
    """
    Fonction qui retourne le contenu de tout le fichier en une seule chaine de caracteres 
    :param: le fichier et son répertoire
    :return: une chaine de caracteres qui represente tout le contenu du fichier 
    :rtype: string ( chaine de caracteres )
    """
    if directory[-1] != '/':
        directory += '/'
    with open(directory+file, 'r') as f:
        return ''.join(f.readlines())
    

def calculate_occurence_words(string):
    """
    Fonction qui retourne un dictionnaire dont la clé est le mot et sa valeur est le nombre d'occurence pour chaque fichier
    :param: une chaine de caractere ( elle represente tout le contenu du fichier apres nettoyage )
    :return: dictionnaire {mot : nbOccurence}
    :rtype: dictionnaire
    """
    nb_occurence = {}
    for word in string.split():
        if word not in nb_occurence:
            nb_occurence[word] = 1
        else:
            nb_occurence[word] += 1
    return nb_occurence


def TfIdf_Matrice(directory='./cleaned/'):
    """
    Fonction qui retourne une matrice TF-IDF dont chaque ligne represente un mot et son score TF-IDF dans chaque fichier (en colonne) 
    :param: répertoire des fichiers textes nettoyés 
    :return: Matrice (ligne = mot , colonne = fichier, et score TF-IDF pour chaque ligne dans chaque colonne)
    :rtype: Matrice
    """
    list_files = list_of_files(directory, '.txt')
    matrice = [[files.replace('_cleaned', '') for files in list_files]]
    matrice[0].insert(0, '')
    idf = CalculateIDF()
    allWords = set().union(*create_file_words_dict().values())
    files_tf = {file: calculate_occurence_words(file_reader(file, directory)) for file in list_files}
    for word in allWords:
        line = [word]
        for file in list_files:
            tf = files_tf[file]
            if word not in tf:
                tf[word] = 0
            line.append(tf[word] * idf[word])
        matrice.append(line)
    return matrice


def create_file_words_dict(directory="./cleaned/"):
    """
    Fonction qui retourne un dictionnaire { fichier : set(mots dans ce fichier}.
    :param: répertoire des fichiers textes nettoyés
    :return: dictionnaire dont la clé est le ficheir et la valeur de cette clé est un set de tous les mots contenant dans ce fichier
    :rtype: dictionnaire
    """
    list_files = list_of_files(directory, ".txt")
    file_words = {}
    for file in list_files:
        words_in_file = set(file_reader(file,directory).split())
        file_words[file] = words_in_file
    return file_words


def CalculateIDF(directory="./cleaned/"):
    """
    Fonction qui retourne un dictionnaire {mot : score IDF}
    :param: répertoire des fichiers textes nettoyés
    :return: dictionnaire dont les clés sont tous les mots dans tous les fichiers et la valeur de chaque clé est le score IDF 
    :rtype: dictionnaire 
    """
    file_words=create_file_words_dict(directory)
    list_files = list_of_files(directory, ".txt")
    allWords = set().union(*file_words.values())
    nb_IDF_words = {}
    for ele in allWords:
        nb_word_existence = 0
        for file in list_files:
            if ele in file_words[file]:  
                nb_word_existence += 1
        nb_IDF_words[ele] = log10(((len(list_files)) / (nb_word_existence)))
    return nb_IDF_words