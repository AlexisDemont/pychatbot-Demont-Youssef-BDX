from TfIdf import TfIdf_Matrice

def NotImportantWord(directory="./cleaned/"):
    """
    Fonction qui retourne un set des mots dont le score TfIdf = 0 pour l'ensemble des textes
    :param: répertoire des fichiers textes nettoyés
    :return: set des mots dont le score TfIdf = 0 pour l'ensemble des textes
    :rtype: set
    """
    matrice = TfIdf_Matrice(directory)
    NotImportantsWords = set()
    for i in range(1, len(matrice)):
        currentWord = matrice[i][0]
        isNull = True
        for j in range(1, len(matrice[i])):
            if matrice[i][j] != 0:
                isNull = False
        if isNull:
            NotImportantsWords.add(str(currentWord))
    return NotImportantsWords