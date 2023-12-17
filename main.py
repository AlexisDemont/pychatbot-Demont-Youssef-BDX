from words_classifier import most_important_word, not_important_word, word_most_spoken, find_who_said_first_this, find_all_pertinent_said_words,calculate_president_most_said_word, speaker_of_word
from text_organization import speeches_cleaner
import os
import PySimpleGUI as sg


speeches_cleaner()

try:
    os.mkdir("./cleaned/")
except FileExistsError:
    pass


dateText = {
    "Giscard dEstaing": 1974,
    "Mitterrand": 1981,
    "Chirac1": 1995,
    "Chirac2": 2002,
    "Sarkozy": 2007,
    "Hollande": 2012,
    "Macron": 2017,
}



print("Bienvenue dans le programme de traitement de discours")
print("Avant de démarrer veuillez renseigner quelques paramètres")

#ask for a directory with pysimplegui
speeches=""


#check if the directory exist, if not ask for a new one and put a message in red saying that the directory is invaliddirectory
current_state = 0
sg.theme('DarkAmber')
layout = [[sg.Text('Veuillez selectionner le dossier contenant les discours', text_color='red')],
              [sg.Text('Dossier', size=(8, 1)), sg.Input(), sg.FolderBrowse()],
              [sg.Submit(), sg.Exit()]]  

window = sg.Window('Paramètres', layout)
while not os.path.isdir(speeches):
    event, values = window.read()
    speeches = values[0]
    if event == sg.WIN_CLOSED or event == 'Exit':
        #nb : l'utilisation de break est recommandé dans la documentation de pysimplegui
        break
window.close()

choices = ('Fonctionnalités de la partie 1', 'Fonctionnalités de la partie 2')

layout = [  [sg.Text('Que voulez vous faire ?')],
            [sg.Listbox(choices, size=(30, len(choices)), key='-FirstChoice-')],
            [sg.Button('Ok')]  ]

window = sg.Window('Menu principal', layout)


while True:                  
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-FirstChoice-']:   
            user_choice = values['-FirstChoice-'][0]
            break
window.close()

#get the index of the user_choice
if user_choice == 'Fonctionnalités de la partie 1':
    choices = ('Les mots les moins importants dans le document', 
                'Les mots ayant le score TD-IDF le plus élevé',
                'Les mots les plus répétés par le président Chirac',
                'Les noms des présidents qui ont parlé de la Nation et celui qui l\'a répété le plus de fois',
                'Le premier president à parler du climat et/ou l\'écologie',
                'Les mots évoqués par tous les présidents'           
                        )
    layout = [  [sg.Text('Que souhaitez-vous afficher ?')],
            [sg.Listbox(choices, size=(30, len(choices)), key='-PartOne-')],
            [sg.Button('Ok')]  ]
    window = sg.Window('Menu principal', layout)


    while True:                  # the event loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            if values['-FirstChoice-']:    # if something is highlighted in the list
                sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
    window.close()

elif user_choice == 'Fonctionnalités de la partie 2':
    





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
