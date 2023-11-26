from motsnonimportants import NotImportantWord
from TF import extractWordsFromThis
from basicsFunctions import file_reader
from president import regroupTextFromSimilarPresidents

def findAllPertinentSaidWords(directory="./cleaned/"):
    textToAnalyze = regroupTextFromSimilarPresidents(directory)
    initialized=False
    saidWords = set()
    tempSet = set()
    nonImportantWord=NotImportantWord()
    for key in textToAnalyze.keys():
        for file in textToAnalyze[key]:
            for word in extractWordsFromThis(file_reader(file, directory)):
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