import os
import re
from utils import list_of_files

# Dict. pour {fillnames : names}

dict_names = {
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas",
}

def extractTheNameFromThis(filename):
    name = filename
    if '_' in filename:
        name = name.split("_")[1]
    if '.' in filename:
        name = name.split(".")[0]
    for character in name:
        if character.isnumeric():
            name = name.split(character)[0]
    return name



def list_of_names():
    """
    Fonction qui retourne la liste des noms des presidents à partir de la liste list_of_files importée de basics_functions
    :param: pas de paramètre 
    :return: liste de noms de tous les presidents dans speeches
    :rtype: liste
    """
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    presidents_names = set()
    for filename in files_names:
        name = extractTheNameFromThis(filename)
        presidents_names.add(name)
    return presidents_names


def list_of_names_fillnames():
    """
    Fonction qui retourne un set des prenoms noms des presidents
    :param: pas de parametre 
    :return: set des prenoms noms des presidents
    :rtype: set
    """
    presidents_fullname = set()
    presidents_names = list_of_names()
    for name in presidents_names:
        fullName=sayWhatIsTheFullNameOf(name, dict_names)
        presidents_fullname.add(fullName)
    return presidents_fullname


def sayWhatIsTheFullNameOf(name, dict_names):
    name=extractTheNameFromThis(name)
    fullName='Anonyme Anonyme'
    for key in dict_names:
        if name in key:
            fullName=str(dict_names[name] + " " + name)
    return str(fullName)

def regroupTextFromSimilarPresidents(directory='cleaned'):
    authorsName = list_of_names()
    list_files = list_of_files(directory, ".txt")
    dict_files = {}
    for author in authorsName:
        dict_files[author] = [file for file in list_files if author in file]
    return dict_files

def speeches_to_lowercase(directory, extension):
    """
    Fonction qui retourne Vrai lorsque la conversion des textes en minuscule soit effectuée
    :param: répertoire des fichiers , et leur extension 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
    files_names = list_of_files(directory, extension)
    for name in files_names:
        newName = name.split('.')[0] + '_lowercased.txt'
        with open('./speeches/' + name, 'r') as rawText, open('./cleaned/' + newName, 'w') as minimizedText:
            for line in rawText:
                line = line.lower()
                minimizedText.write(line)
    return


def lowercase_to_clean(directory='./cleaned/', extension='.txt'):
    """
    Fonction qui retourne Vrai lorsque chaque caractere non numeric et non alphabetique soit remplacé par des espaces  
    :param: répertoire des fichiers textes nettoyés 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
    files_names = list_of_files(directory, extension)
    for name in files_names:
        newName = name.replace('lowercased', 'cleaned')
        if 'lowercased' in name:
            with open(directory + name, 'r') as lowercasedText, open(directory + newName, 'w') as cleanedText:
                for line in lowercasedText:
                    for character in line:
                        if not (character.isalpha()) and not (character.isnumeric()):
                            line = line.replace(character, ' ')
                    line = re.sub(' +', ' ', line)
                    line = line.lstrip()
                    cleanedText.write(line)
            os.remove(directory + name)
    return


def speechesCleaner(directory='./speeches/', extension='.txt'):
    """
    Fonction qui retourne Vrai lorsque les deux fonctions precedentes qui y sont incluses ont été effectuées  
    :param: répertoire des fichiers textes nettoyés 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
    speeches_to_lowercase(directory, extension)
    lowercase_to_clean()
    return
