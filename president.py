# Extraire les noms des présidents à partir des fichiers texte fournis
from basicsFunctions import list_of_files

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




"""
    Fonction qui retourne un set des prenoms noms des presidents
    :param: pas de parametre 
    :return: set des prenoms noms des presidents
    :rtype: set
    """


def list_of_names_fillnames():
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