# A partir de la matrice on crée un set des mots dont le score TfIdf= 0
from TfIdf import TfIdf_Matrice

def NotImportantWord():
    matrice = TfIdf_Matrice(directory="./cleaned/")
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