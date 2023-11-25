import os
import re
from basicsFunctions import list_of_files
"""
    Fonction qui retourne Vrai lorsque la conversion des textes en minuscule soit effectuée
    :param: répertoire des fichiers , et leur extension 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
def speeches_to_lowercase(directory, extension):
    files_names = list_of_files(directory, extension)
    for name in files_names:
        newName = name.split('.')[0] + '_lowercased.txt'
        with open('./speeches/' + name, 'r') as rawText, open('./cleaned/' + newName, 'w') as minimizedText:
            for line in rawText:
                line = line.lower()
                minimizedText.write(line)
    return True

"""
    Fonction qui retourne Vrai lorsque chaque caractere non numeric et non alphabetique soit remplacé par des espaces  
    :param: répertoire des fichiers textes nettoyés 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
def lowercase_to_clean(directory='./cleaned/', extension='.txt'):
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
    return True

"""
    Fonction qui retourne Vrai lorsque les deux fonctions precedentes qui y sont incluses ont été effectuées  
    :param: répertoire des fichiers textes nettoyés 
    :return: Vrai lorsque la fonction est finie
    :rtype: Booléen
    """
def speechesCleaner(directory='./speeches/', extension='.txt'):
    speeches_to_lowercase(directory, extension)
    lowercase_to_clean()
    return True
