import os

"""
    Fonction qui retourne une liste dont les elements sont les noms des fichiers qui se trouve dans repertoire et se terminent par des extensions precis 
    :param: répertoire et extension
    :return: liste des noms des fichiers 
    :rtype: liste
    """
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

"""
    Fonction qui retourne vrai lorsque la suppression de tous les fichiers de la liste 'list_of_files' dans le repertoire cleaned et dont l'extension (txt), a été effectuée 
    :param: répertoire des fichiers textes nettoyés, et extension (txt)
    :return: True lorsque la suppression de tous les fichers dans la liste files_name dans le repertoire cleaned (txt)
    :rtype: Booléen
    """
def clean_folder(directory='./cleaned', extension='txt'):
    files_names = list_of_files(directory, extension)
    for name in files_names:
        os.remove(directory + name)
    return True

"""
    Fonction qui retourne le contenu de tout le fichier en une seule chaine de caracteres 
    :param: le fichier et son répertoire
    :return: une chaine de caracteres qui represente tout le contenu du fichier 
    :rtype: string ( chaine de caracteres )
    """
def file_reader(file,directory):
    if directory[-1] != '/':
        directory += '/'
    with open(directory+file, 'r') as f:
        return ''.join(f.readlines())