" importer la liste des mots fct1 "
from utils import create_file_words_dict
from text_organization import string_cleaner


def SearchCommonWords (string , directory) :
    """
        Function that returns a list of commons words between the question and the documents

        Parameters:
            A string and directory

        Returns:
            list of common words

        """
    WordString = string_cleaner(string)

    file_words = create_file_words_dict(directory)
    all_words = set().union(*file_words.values())

    CommonWords = []
    for element in WordsInQuestion :
        if element in all_words :
            CommonWords.append(element)

    return CommonWords
