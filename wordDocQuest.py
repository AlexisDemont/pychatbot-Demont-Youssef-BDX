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
        if element in tfidf_matrice(directory) :
            CommonWords.append(element)

    return CommonWords
test = print(SearchCommonWords("le climat ", './cleaned/'))
# le probleme vient apparemment de la matrice tf-idf car si on teste tf idf dans utils il y a un souci