from utils import file_reader, list_of_files, tfidf_matrice, calculate_occurence_words,create_file_words_dict
from text_organization import regroup_text_from_similar_speakers, list_of_names_fillnames, extract_the_name_from_this, string_cleaner

def most_important_word(directory="./cleaned/"):
    """
    Function that returns a set of the most important words based on the sum of their TfIdf scores across all texts.

    Parameters:
        directory (str): Path to the directory of cleaned text files.

    Returns:
        most_importants_words (set): Set of the most important words.

    """
    matrice = tfidf_matrice(directory)
    most_importants_words = set()
    highest_score = 0
    for i in range(1, len(matrice)):
        current_word = matrice[i][0]
        sum_score = 0
        for j in range(1, len(matrice[i])):
            sum_score += matrice[i][j]
        if sum_score > highest_score:
            highest_score = sum_score
            most_importants_words = {str(current_word)}
        elif sum_score == highest_score:
            most_importants_words.add(str(current_word))
    return most_importants_words


def not_important_word(directory="./cleaned/"):
    """
    Function that returns a set of words with a TfIdf score of 0 across all texts.

    Parameters:
        directory (str): Path to the directory of cleaned text files.

    Returns:
        not_importants_words (set): Set of words with a TfIdf score of 0.

    """
    matrice = tfidf_matrice(directory)
    not_importants_words = set()
    for i in range(1, len(matrice)):
        current_word = matrice[i][0]
        is_null = True
        for j in range(1, len(matrice[i])):
            if matrice[i][j] != 0:
                is_null = False
        if is_null:
            not_importants_words.add(str(current_word))
    return not_importants_words

def find_who_said_first_this(word, date_text, directory="./cleaned/"):
    """
    Find the first speaker who said a specific word.

    Parameters:
        word (str): The word to search for.
        date_text (dict): A dictionary containing the name of the president and the date of the speech.
        directory (str): Path to the directory of cleaned text files.

    Returns:
        the_first_one (str): The name of the first speaker who said the word.
        year (str): The year when the word was first said.

    """
    the_first_one = ""
    found = False
    word = word.lower()

    for file in list_of_files(directory, ".txt"):
        current_file = file_reader(file, "./cleaned")
        if word in current_file:
            for key in date_text.keys():
                if key in file:
                    if not found:
                        found = True
                        the_first_one = (key, date_text[key])
                    elif date_text[key] < date_text[the_first_one[0]]:
                        the_first_one = (key, date_text[key])
    if found:
        year = the_first_one[1]
        the_first_one = extract_the_name_from_this(the_first_one[0])
    return the_first_one, year


def find_all_pertinent_said_words(directory="./cleaned/"):
    """
    Find all the pertinent words said by the speakers.

    Parameters:
        directory (str): Path to the directory of cleaned text files.

    Returns:
        said_words (set): Set of all the pertinent words said by the speakers.

    """
    text_to_analyze = regroup_text_from_similar_speakers(directory)
    initialized = False
    said_words = set()
    temp_set = set()
    non_important_word = not_important_word()
    for key in text_to_analyze.keys():
        for file in text_to_analyze[key]:
            for word in file_reader(file, directory).split():
                if word not in non_important_word:
                    temp_set.add(str(word))
        if not initialized:
            said_words = temp_set.copy()
            initialized = True
            temp_set.clear()
        else:
            said_words = said_words.intersection(temp_set)
            temp_set.clear()
    return said_words

def speaker_of_word(word):
    """
    Find the speakers who said a specific word.

    Parameters:
        word (str): The word to search for.

    Returns:
        speaker (dict): A dictionary containing the speakers and the number of times they said the word.

    """
    word = word.lower()
    directory = './cleaned/'
    list_files = list_of_files('./cleaned', '.txt')
    files_tf = {file: calculate_occurence_words(file_reader(file, directory)) for file in list_files}
    speaker = {}
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


def word_most_spoken(word):
    """
    Find the speaker who spoke the most times a specific word.

    Parameters:
        word (str): The word to search for.

    Returns:
        president (str): The name of the speaker who spoke the most times the word.

    """
    speakers = speaker_of_word(word)
    maxi = 0
    president = None
    for key in speakers.keys():
        if speakers[key] > maxi:
            maxi = speakers[key]
            president = key
    if president == None:
        return "Aucun président n'a utilisé ce mot"
    return president


def calculate_president_most_said_word(president_name):
    """
    Calculate the most frequently spoken word by a specific president.

    Parameters:
        president_name (str): The name of the president.

    Returns:
        president_most_said_words (set): Set of the most frequently spoken words by the president.

    """
    president_word_occurence = {}
    president_most_said_words = set()
    max_occurence = 0
    exist = 0

    president_name = president_name.lower()
    list_existing_files = list_of_files("./cleaned", ".txt")
    for file in list_existing_files:
        if president_name in file.lower():
            exist = 1
            occurence_temp = calculate_occurence_words(file_reader(file, "./cleaned"))
            for key in occurence_temp.keys():
                if key in president_word_occurence.keys():
                    president_word_occurence[key] += occurence_temp[key]
                else:
                    president_word_occurence[key] = occurence_temp[key]
    if not exist:
        raise ValueError("President name not found")
    for key in president_word_occurence.keys():
        if president_word_occurence[key] > max_occurence:
            max_occurence = president_word_occurence[key]
            president_most_said_words = {key}
        elif president_word_occurence[key] == max_occurence:
            president_most_said_words.add(key)
    return president_most_said_words




def search_common_words (string , directory) :
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
    for element in WordString :
        if element in all_words :
            CommonWords.append(element)

    return CommonWords
