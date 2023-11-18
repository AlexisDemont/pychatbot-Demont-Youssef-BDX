# A partir de la matrice on crée un set des mots dont le score TfIdf= 0
from TfIdf import TfIdf_Matrice
def NotImportantWord():
    matrice = TfIdf_Matrice(directory='./cleaned/')
    matrice[0].insert(0, " ")
    for word in matrice :
        NotImportantsWords = set()
        for ScoreWord in word :
            if ScoreWord == 0 :
                zero = 0
        if zero == 0 :
            NotImportantsWords.update(word)
    return NotImportantsWords