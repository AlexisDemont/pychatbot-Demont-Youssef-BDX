import os

clean_directory = "/cleaned/*"


try:
    os.mkdir("./cleaned/")
except FileExistsError:
    pass

from words_classifier import (
    most_important_word,
    not_important_word,
    find_who_said_first_this,
    find_all_pertinent_said_words,
    calculate_president_most_said_word,
    speaker_of_word,
)
from utils import directory_cleaner
from text_organization import speeches_cleaner, find_text_categories

import PySimpleGUI as sg
from answer_generation import generate_answer_to_this


dict_names = {
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas",
}

dateText = {
    "Giscard dEstaing": 1974,
    "Mitterrand": 1981,
    "Chirac1": 1995,
    "Chirac2": 2002,
    "Sarkozy": 2007,
    "Hollande": 2012,
    "Macron": 2017,
}

presidents = tuple((dict_names[key] + " " + key) for key in dict_names.keys())

current_state = 0
# 0 : initialisation, 1 : choix des fonctionnalités, 2 : choix des fonctionnalités de la partie 1
# 3 : mot le plus prononcé par un président,  4 : choix des textes du chatbot 5 : chatbot


menu_def = [["File", ["Exit"]]]
sg.theme("DarkAmber")
sg.set_options(element_padding=(0, 0))

# nb : l'utilisation de break est recommandé dans la documentation de pysimplegui
while current_state < 9:
    if current_state == 0:
        speeches = ""

        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [
                sg.Text(
                    "Veuillez selectionner le dossier contenant les discours",
                    text_color="red",
                ),
            ],
            [sg.Text("Dossier", size=(8, 1)), sg.Input(), sg.FolderBrowse()],
            [sg.Submit(), sg.Exit()],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Paramètres",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)
        while not os.path.isdir(speeches):
            event, values = window.read()
            if event == "Submit":
                speeches = values[1]
                if speeches.lower() == "toto":
                    sg.popup(
                        "Very predictable Mister JAD",
                        title="Easter egg",
                        auto_close=True,
                        auto_close_duration=5,
                        keep_on_top=True,
                        line_width=100,
                    )
            if event == sg.WIN_CLOSED or event == "Exit":
                speeches = ""
                current_state = 10
                break
        current_state += 1
        window.close()

    if current_state == 1:
        choices = ("Fonctionnalités de la partie 1", "Le chatbot")

        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text("Que voulez vous faire ?")],
            [sg.Listbox(choices, size=(30, len(choices)), key="-FIRSTCHOICE-")],
            [sg.Button("Ok"), sg.Button("Retour")],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Choix des fonctionnalités",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)
        window["-FIRSTCHOICE-"].expand(expand_x=True, expand_y=True)

        while True:
            event, values = window.read()
            if event == "Ok":
                if values["-FIRSTCHOICE-"]:
                    user_choice = values["-FIRSTCHOICE-"][0]
                    if user_choice == "Fonctionnalités de la partie 1":
                        current_state += 1
                    elif user_choice == "Le chatbot":
                        current_state += 3
                    break
            if event == "Retour":
                current_state -= 1
                break
            if event == sg.WIN_CLOSED or event == "Exit":
                current_state = 10
                break
        window.close()

    # get the index of the user_choice
    if current_state == 2:
        directory_cleaner(clean_directory)
        speeches_cleaner()
        choices = (
            "Les mots les moins importants des documents",
            "Les mots ayant le score TD-IDF le plus élevé",
            "Les mots les plus répétés par un président",
            "Les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois",
            "Le premier president à parler du climat et/ou l'écologie",
            "Les mots évoqués par tous les présidents",
        )
        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text("Que souhaitez-vous afficher ?")],
            [
                sg.Listbox(
                    choices,
                    size=(80, len(choices)),
                    key="-CHOICES-",
                    auto_size_text=True,
                )
            ],
            [sg.Button("Ok"), sg.Button("Retour")],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Choix de la partie 1",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)
        window["-CHOICES-"].expand(expand_x=True, expand_y=True)

        while True:
            event, values = window.read()
            if event == "Ok":
                if values["-CHOICES-"]:
                    if (
                        values["-CHOICES-"][0]
                        == "Les mots les moins importants des documents"
                    ):
                        sg.popup(
                            f"Les mots les moins importants du corpus sont : {not_important_word(directory='./cleaned/')}",
                            title="Mots les plus importants",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
                    elif (
                        values["-CHOICES-"][0]
                        == "Les mots ayant le score TD-IDF le plus élevé"
                    ):
                        sg.popup(
                            f"Les mots les plus importants du corpust sont : {most_important_word(directory='./cleaned/')}",
                            title="Mots les moins importants",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
                    elif (
                        values["-CHOICES-"][0]
                        == "Les mots les plus répétés par un président"
                    ):
                        current_state += 1
                        break
                    elif (
                        values["-CHOICES-"][0]
                        == "Les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus de fois"
                    ):
                        sg.popup(
                            f"Les présidents ayant utilisé le mot Nation sont : {speaker_of_word('Nation')}",
                            title="Présidents ayant parlé de la Nation",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
                    elif (
                        values["-CHOICES-"][0]
                        == "Le premier president à parler du climat et/ou l'écologie"
                    ):
                        the_first_one = find_who_said_first_this("climat", dateText)
                        sg.popup(
                            f"Le premier president à parler de l'écologie/climat est : {the_first_one[0]} en {the_first_one[1]}",
                            title="Premier président à parler de l'écologie/climat",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
                    elif (
                        values["-CHOICES-"][0]
                        == "Les mots évoqués par tous les présidents"
                    ):
                        sg.popup(
                            f"Les mots évoqués par tous les présidents sont : {find_all_pertinent_said_words()}",
                            title="Mots évoqués par tous les présidents",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
            if event == "Retour":
                current_state -= 1
                break
            if event == sg.WIN_CLOSED or event == "Exit":
                current_state = 10
                break

        window.close()

    if current_state == 3:
        choices = presidents

        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text("Que voulez vous faire ?")],
            [sg.Listbox(choices, size=(30, len(choices)), key="-PRESIDENTS-")],
            [sg.Button("Ok"), sg.Button("Retour")],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Mot le plus répété",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)
        window["-PRESIDENTS-"].expand(expand_x=True, expand_y=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Ok":
                if values["-PRESIDENTS-"]:
                    user_choice = values["-PRESIDENTS-"][0]
                    sg.popup(
                        f"Les mots les plus répétés par le président {values['-PRESIDENTS-'][0]} : {calculate_president_most_said_word(values['-PRESIDENTS-'][0].split()[-1].lower())}",
                        title="Mots les moins répétés par ",
                        auto_close=True,
                        auto_close_duration=30,
                        keep_on_top=True,
                        line_width=100,
                    )
            if event == "Retour":
                current_state -= 1
                break
            if event == sg.WIN_CLOSED or event == "Exit":
                current_state = 10
                break
        window.close()
    if current_state == 4:
        choices = tuple()
        for ele in find_text_categories(speeches, "txt"):
            choices = choices + (ele,)
        choices = ("Tous les textes",) + choices
        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text("Quelle(s) catégorie(s) souhaitez vous ?")],
            [sg.Listbox(choices, size=(30, len(choices)), key="-TEXTCHOICE-")],
            [sg.Button("Ok"), sg.Button("Retour")],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Choix des fonctionnalités",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)
        window["-TEXTCHOICE-"].expand(expand_x=True, expand_y=True)

        while True:
            event, values = window.read()
            if event == "Ok":
                if values["-TEXTCHOICE-"]:
                    user_choice = values["-TEXTCHOICE-"][0]
                    if user_choice == "Tous les textes":
                        user_choice = False
                    current_state += 1
                    break
            if event == "Retour":
                current_state -= 3
                break
            if event == sg.WIN_CLOSED or event == "Exit":
                current_state = 10
                break
        window.close()

    if current_state == 5:
        directory_cleaner(clean_directory)
        speeches_cleaner(user_choice)
        elements = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text("Veuillez poser votre question")],
            [sg.InputText()],
            [sg.Button("Ok"), sg.Button("Retour")],
        ]

        layout = [
            [sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))],
            [
                sg.Text("", pad=(0, 0), key="-EXPAND2-"),
                sg.Column(
                    elements,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
            ],
        ]

        window = sg.Window(
            "Chatbot",
            layout,
            resizable=True,
            default_element_size=(40, 1),
            element_justification="center",
            finalize=True,
        )
        window["-C-"].expand(True, True, True)
        window["-EXPAND-"].expand(True, True, True)
        window["-EXPAND2-"].expand(True, False, True)

        while True:
            event, values = window.read()
            if event == "Ok":
                if values[1]:
                    user_choice = values[1]
                    if user_choice.lower() == "toto":
                        sg.popup(
                            f"Je trouve les blagues de toto terriblement nulles",
                            title="Réponse à votre question",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
                    else:
                        sg.popup(
                            f"{generate_answer_to_this(user_choice)}",
                            title="Réponse à votre question",
                            auto_close=True,
                            auto_close_duration=30,
                            keep_on_top=True,
                            line_width=100,
                        )
            if event == "Retour":
                current_state -= 1
                break
            if event == sg.WIN_CLOSED or event == "Exit":
                current_state = 10
                break
        window.close()
