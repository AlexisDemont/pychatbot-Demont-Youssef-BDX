from words_classifier import most_important_word, not_important_word, word_most_spoken, find_who_said_first_this, find_all_pertinent_said_words,calculate_president_most_said_word, speaker_of_word
from text_organization import speeches_cleaner
speeches_cleaner()
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
    print(f"Les mots les moins importants dans le document sont : {not_important_word(directory='./cleaned/')}")
elif InputValue == 1 :
    print(f"Les mots ayant le score TD-IDF le plus élevé sont : {most_important_word(directory='./cleaned/')}")
elif InputValue == 2 :
    print(f"Les mots les plus répétés par le président Chirac sont :")
    most_said_words=calculate_president_most_said_word('chirac')
    for word in most_said_words:
        print(word)
elif InputValue == 3 :
    speakers=speaker_of_word('Nation')
    who_said_it_most=word_most_spoken('Nation')
    
    print("Les présidents ayant utilisé le mot Nation sont :")
    for speaker in speakers:
        print(speaker)
    print(f"Le président ayant le plus utilisé le mot Nation est : {who_said_it_most}")
elif InputValue == 4 :
    name,year=find_who_said_first_this('climat',dateText)
    print(f"Le premier president à parler de l'écologie/climat est : {name} en {year}")  
elif InputValue == 5 :
    print(f"Les mots évoqués par tous les présidents : {find_all_pertinent_said_words()}")
