from basicsFunctions import list_of_files, file_reader
from TF import CalculateOccurenceWords
from IDF import CalculateIDF, create_file_words_dict, RegroupAllWords


"""
    Fonction qui retourne une matrice TF-IDF dont caque ligne represente un mot et son score TF-IDF dans chaque fichier (en colonne) 
    :param: répertoire des fichiers textes nettoyés 
    :return: Matrice (ligne = mot , colonne = fichier, et score TF-IDF pour chaque ligne dans chaque colonne)
    :rtype: Matrice
    """
def TfIdf_Matrice(directory='./cleaned/'):
    list_files = list_of_files('./cleaned', '.txt')
    matrice = [[files.replace('_cleaned', '') for files in list_files]]
    matrice[0].insert(0, '')
    idf = CalculateIDF()
    file_words = create_file_words_dict()
    allWords = RegroupAllWords(file_words)
    files_tf = {file: CalculateOccurenceWords(file_reader(file, directory)) for file in list_files}
    for word in allWords:
        line = [word]
        for file in list_files:
            tf = files_tf[file]
            if word not in tf:
                tf[word] = 0
            line.append(tf[word] * idf[word])
        matrice.append(line)
    return matrice