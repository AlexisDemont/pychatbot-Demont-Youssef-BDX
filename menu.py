# Menu je ne vois pas les autres fonctions
from motsnonimportants import NotImportantWord
from motsplusimportant import mostImportantWord

print("Pour afficher les mots les moins importants dans le document , Tapez 0")
print("Pour afficher les mots ayant le score TD-IDF le plus élevé , Tapez 1")
print("Pour afficher les mots les plus répétés par le président Chirac , Tapez 2")
print("Pour afficher les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois , Tapez 3")
print("Pour afficher le premier president à parler du climat et/ou l'écologie , Tapez 4")
print("Pour afficher les mots évoqués par tous les présidents , Tapez 5 ")

InputValue = int(input("Veuillez choisir la fonctionnalité souhaitée : "))

if InputValue == 0 :
    print("Les mots les moins importants dans le document sont :",NotImportantWord(directory="./cleaned/"))
elif InputValue == 1 :
    print("Les mots ayant le score TD-IDF le plus élevé sont :"mostImportantWord(directory="./cleaned/"))
elif InputValue == 2 :
    print("Les mots les plus répétés par le président Chirac sont :")
elif InputValue == 3 :
    print("Les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois :")
elif InputValue == 4 :
    print("Le premier president à parler du climat et/ou l'écologie est :")
elif InputValue == 5 :
    print("Les mots évoqués par tous les présidents :")
