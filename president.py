# Extraire les noms des présidents à partir des fichiers texte fournis
from basicsFunctions import list_of_files

# Fonction definie pour extraire que les noms des presidents ( sans Nomination_"".txt)
def list_of_names():
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    presidents_names = set()
    for filename in files_names:
        name = filename.split('_')[1]
        name = name.split('.')[0]
        for character in name:
            if character.isnumeric():
                name = name.split(character)[0]
        presidents_names.add(name)
    return presidents_names


# Dict. pour {fillnames : names}

dict_names_fillnames = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Holland": "François", "Macron": "Emmanuel",
                        "Mitterrand": "François", "Sarkozy": "Nicolas"}


# Fonction associer à chaque nom son prénom

def list_of_names_fillnames():
    presidents_firstname_name = set()
    presidents_names = list_of_names()
    for president in presidents_names:
        for name in dict_names_fillnames:
            if president == name:
                presidents_firstname_name.add(dict_names_fillnames[name] + " " + name)
    return presidents_firstname_name