# Menu je ne vois pas les autres fonctions
from motsnonimportants import NotImportantWord
from motsplusimportant import mostImportantWord
from NationNbFois import WordMostSpoken
from NationNbFois import WordMostSpoken
from climatEcologie import findWhoSaidFirstThis
from presidentwordmostspoken import calculatePresidentMostSaidWord
from allSaidWord import findAllPertinentSaidWords

dateText = {
    "Giscard dEstaing": 1974,
    "Mitterrand": 1981,
    "Chirac1": 1995,
    "Chirac2": 2002,
    "Sarkozy": 2007,
    "Hollande": 2012,
    "Macron": 2017,
}

print("Pour afficher les mots les moins importants dans le document , Tapez 0")
print("Pour afficher les mots ayant le score TD-IDF le plus élevé , Tapez 1")
print("Pour afficher les mots les plus répétés par le président Chirac , Tapez 2")
print("Pour afficher les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois , Tapez 3")
print("Pour afficher le premier president à parler du climat et/ou l'écologie , Tapez 4")
print("Pour afficher les mots évoqués par tous les présidents , Tapez 5 ")

InputValue = int(input("Veuillez choisir la fonctionnalité souhaitée : "))

if InputValue == 0 :
    print(f"Les mots les moins importants dans le document sont : {NotImportantWord(directory='./cleaned/')}")
elif InputValue == 1 :
    print(f"Les mots ayant le score TD-IDF le plus élevé sont : {mostImportantWord(directory='./cleaned/')}")
elif InputValue == 2 :
    print(f"Les mots les plus répétés par le président Chirac sont : {calculatePresidentMostSaidWord('chirac')}",)
elif InputValue == 3 :
    print(f"Les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois : {WordMostSpoken('Nation')}")
elif InputValue == 4 :
    name,year=findWhoSaidFirstThis('climat',dateText)
    print(f"Le premier president à parler de l'écologie/climat est : {name} en {year}")  
elif InputValue == 5 :
    print(f"Les mots évoqués par tous les présidents : {findAllPertinentSaidWords()}")
