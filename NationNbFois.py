#  Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
from TfIdf import TfIdf_Matrice
# dictionnaire {president : nbFoisMot}
def SpeakerOfWord (word):
    Matrice = TfIdf_Matrice(directory='./cleaned/')
    trouve = True
    i = 0
    speakers = {}
    While not trouve :
        if word == Matrice[i][0]:
            trouve = True
            for j in range (1,len(Matrice[i])-1):
                if Matrice[i][j] != 0 :
                    speakers[Matrice[0][j]] = Matrice[i][j]
    return speakers

#Comparaison entre les clés et return le president qui prononce le mot le plus de fois
def WordMostSpoken ():
    speakers = SpeakerOfWord(word)
    maxi = 0
    for key in speakers.keys():
        print(key)
        if speaker[key] > maxi :
            maxi = speaker[key]
            president = key
    return president

