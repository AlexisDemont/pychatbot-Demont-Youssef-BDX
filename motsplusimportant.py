from TfIdf import TfIdf_Matrice
def mostImportantWord(directory="./cleaned/"):
    """
    Fonction qui retourne un set des mots dont la somme des scores TfIdf pour l'ensemble des textes est la plus élevée
    :param: répertoire des fichiers textes nettoyés
    :return: set des mots les plus importants sur l'ensemble des textes
    :rtype: set
    """
    matrice = TfIdf_Matrice(directory)
    mostImportantsWords = set()
    highestScore=0
    for i in range(1, len(matrice)):
        currentWord = matrice[i][0]
        sumScore=0
        for j in range(1, len(matrice[i])):
            sumScore += matrice[i][j]
        if sumScore > highestScore:
            highestScore = sumScore
            mostImportantsWords = {str(currentWord)}
        elif sumScore == highestScore:
            mostImportantsWords.add(str(currentWord))
    return mostImportantsWords