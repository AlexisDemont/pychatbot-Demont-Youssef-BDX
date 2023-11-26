from NationNbFois import WordMostSpoken
from TF import CalculateOccurenceWords
from basicsFunctions import file_reader, list_of_files
from president import list_of_names_fillnames

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
            occurenceTemp = CalculateOccurenceWords(file_reader(file, "./cleaned"))
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
