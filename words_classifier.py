from utils import file_reader, list_of_files, TfIdf_Matrice, calculate_occurence_words
from words_classifier import extractTheNameFromThis, regroupTextFromSimilarPresidents, list_of_names_fillnames

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

def findWhoSaidFirstThis(word, dateText, directory="./cleaned/"):
    """Find who said first this word
    param: word (str), dateText (dict)
    pre: word is a string, dateText is a dict with the name of the president and the date of the speech, directory is a string
    of the emplacement of cleaned texts
    return: the name of the first one who said the word
    rtype: str"""
    theFirstOne = ""
    found = False
    word = word.lower()

    for file in list_of_files(directory, ".txt"):
        currentFile = file_reader(file, "./cleaned")
        if word in currentFile:
            for key in dateText.keys():
                if key in file:
                    if not found:
                        found = True
                        theFirstOne = (key, dateText[key])
                    elif dateText[key] < dateText[theFirstOne[0]]:
                        theFirstOne = (key, dateText[key])
    if found:
        year=theFirstOne[1]
        theFirstOne = extractTheNameFromThis(theFirstOne[0])
    return theFirstOne,year


def findAllPertinentSaidWords(directory="./cleaned/"):
    textToAnalyze = regroupTextFromSimilarPresidents(directory)
    initialized=False
    saidWords = set()
    tempSet = set()
    nonImportantWord=NotImportantWord()
    for key in textToAnalyze.keys():
        for file in textToAnalyze[key]:
            for word in file_reader(file, directory).split():
                if word not in nonImportantWord:
                    tempSet.add(str(word))
        if not initialized:
            saidWords = tempSet.copy()
            initialized=True
            tempSet.clear()
        else:
            saidWords = saidWords.intersection(tempSet)
            tempSet.clear()
    return saidWords

def SpeakerOfWord(word):
    word = word.lower()
    directory = './cleaned/'
    list_files = list_of_files('./cleaned', '.txt')
    files_tf = {file: calculate_occurence_words(file_reader(file, directory)) for file in list_files}
    speaker={}
    presidents = list_of_names_fillnames()
    for filename in files_tf.keys():
        if word in files_tf[filename]:
            for president in presidents:
                if president.split(' ')[1] in filename:
                    if president in speaker:
                        speaker[president] += files_tf[filename][word]
                    else:
                        speaker[president] = files_tf[filename][word]
    return speaker


def WordMostSpoken(word):
    speakers = SpeakerOfWord(word)
    maxi = 0
    president=None
    for key in speakers.keys():
        if speakers[key] > maxi :
            maxi = speakers[key]
            president = key
    if president == None:
        return "Aucun président n'a utilisé ce mot"
    return president


def calculatePresidentMostSaidWord(presidentName):
    """
    :param presidentName: str
    :return: set
    """
    presidentWordOccurence = {}
    presidentMostSaidWords = set()
    maxOccurence = 0
    exist = 0

    presidentName = presidentName.lower()
    list_existing_files = list_of_files("./cleaned", ".txt")
    for file in list_existing_files:
        if presidentName in file.lower():
            exist = 1
            occurenceTemp = calculate_occurence_words(file_reader(file, "./cleaned"))
            for key in occurenceTemp.keys():
                if key in presidentWordOccurence.keys():
                    presidentWordOccurence[key] += occurenceTemp[key]
                else:
                    presidentWordOccurence[key] = occurenceTemp[key]
    if not exist:
        raise ValueError("President name not found")
    for key in presidentWordOccurence.keys():
        if presidentWordOccurence[key] > maxOccurence:
            maxOccurence = presidentWordOccurence[key]
            presidentMostSaidWords = {key}
        elif presidentWordOccurence[key] == maxOccurence:
            presidentMostSaidWords.add(key)
    return presidentMostSaidWords
