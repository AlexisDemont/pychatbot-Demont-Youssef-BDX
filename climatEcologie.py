from basicsFunctions import file_reader, list_of_files
from president import extractTheNameFromThis



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

    list_files = list_of_files(directory, ".txt")
    for file in list_files:
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
