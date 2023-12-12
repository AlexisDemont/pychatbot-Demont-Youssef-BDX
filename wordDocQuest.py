" importer la liste des mots fct1 "

from utils import tfidf_matrice
def SearchCommonWords (string , directory) :
    """
        Function that returns a list of commons words between the question and the documents

        Parameters:
            A string

        Returns:
            list of common words

        """
    WordsInQuestion = ['le','climat'] # fonction pour la liste des mots
    CommonWords = []
    for element in WordsInQuestion :
        for word in tfidf_matrice (directory) :
            if element == word :
                CommonWords.append(element)

    return CommonWords
test = print(SearchCommonWords("le climat ", './cleaned/'))
