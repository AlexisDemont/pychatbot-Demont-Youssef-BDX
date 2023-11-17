import os

# Fonction definie pour extraire les noms des fichiers à partir des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Fonction pour vider le dossier cleaned
def clean_folder():
    directory = ('./cleaned')
    extension = 'txt'
    files_names = list_of_files(directory, extension)
    for name in files_names:
        os.remove(directory + name)
    return True

def file_reader(file,directory):
    with open(directory+file, 'r') as f:
        return ''.join(f.readlines())
