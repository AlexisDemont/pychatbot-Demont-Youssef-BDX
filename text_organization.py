from utils import list_of_files

dict_names = {
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas",
}


def extract_the_name_from_this(filename):
    """
    Function that extracts the name of the speaker from the filename

    Parameters:
        filename (str): Name of the file

    Returns:
        name (str): Name of the speaker
    """
    name = filename
    if "_" in name:
        name = name.split("_")[1]
    if "." in name:
        name = name.split(".")[0]
    for character in name:
        if character.isnumeric():
            name = name.split(character)[0]
    return name


def list_of_names(directory="./speeches", extension=".txt"):
    """
    Function that returns a set of the names of the speakers in the directory

    Parameters:
        directory (str): Path to the directory
        extension (str): Extension of the files

    Returns:
        names (set): Set of the names of the speakers
    """
    files_names = list_of_files(directory, extension)
    speakers_names = set()
    for filename in files_names:
        name = extract_the_name_from_this(filename)
        speakers_names.add(name)
    return speakers_names


def list_of_names_fillnames():
    """
    Function that returns a set of the full names of the speakers

    Parameters:
        None

    Returns:
        speakers_fullname (set): Set of the full names of the speakers
    """
    speakers_fullname = set()
    speakers_names = list_of_names()
    for name in speakers_names:
        full_name = find_what_is_the_full_name_of(name, dict_names)
        speakers_fullname.add(full_name)
    return speakers_fullname


def find_what_is_the_full_name_of(name, dict_names):
    """
    Function that finds the full name of a given name using a dictionary

    Parameters:
        name (str): Name to find the full name for
        dict_names (dict): Dictionary mapping names to full names

    Returns:
        full_name (str): Full name of the given name
    """
    name = extract_the_name_from_this(name)
    full_name = "Anonyme Anonyme"
    for key in dict_names:
        if name in key:
            full_name = str(dict_names[name] + " " + name)
    return str(full_name)


def regroup_text_from_similar_speakers(directory="cleaned", extension=".txt"):
    """
    Function that regroups text files from similar speakers into a dictionary

    Parameters:
        directory (str): Path to the directory containing the text files
        extension (str): Extension of the text files

    Returns:
        dict_files (dict): Dictionary mapping speaker names to a list of their corresponding files
    """
    authors_name = list_of_names()
    list_files = list_of_files(directory, extension)
    dict_files = {}
    for author in authors_name:
        dict_files[author] = [file for file in list_files if author in file]
    return dict_files


def string_cleaner(string):
    """
    Function that converts a string to clean text

    Parameters:
        string (str): String to clean

    Returns:
        string (str): Cleaned string
    """
    from re import sub
    accent_dict = {"à": "a", "â": "a", "é": "e", "è": "e", "ê": "e", "ë": "e", "î": "i", "ï": "i", "ô": "o", "ö": "o", "ù": "u", "û": "u", "ü": "u", "ç": "c"}
    string = string.lower()
    for character in string:
        if not (character.isalpha()) and not (character.isnumeric()):
            string = string.replace(character, " ")
    for character in accent_dict:
        string = string.replace(character, accent_dict[character])
    string = sub(" +", " ", string)
    string = string.lstrip()
    return string


def speeches_cleaner(directory="./speeches/", extension=".txt"):
    """
    Function that converts speeches to lowercase and remove specials characters

    Parameters:
        directory (str): Path to the directory containing the lowercase text files
        extension (str): Extension of the lowercase text files

    Returns:
        None
    """
    files_names = list_of_files(directory, extension)
    for name in files_names:
        new_name = name.split(".")[0] + "_cleaned.txt"
        with open(directory + "/" + name, "r") as raw_text, open(
            "./cleaned/" + new_name, "w"
        ) as cleaned_text:
            for line in raw_text:
                line = string_cleaner(line)
                cleaned_text.write(line)
    return


def dict_score_TFIDF_question(list):
    from utils import calculate_idf, calculate_occurence_words
    string = "".join(ele + " " for ele in list)
    DictIDF = calculate_idf(directory="./cleaned/", extension=".txt")
    DictTFIDF = calculate_occurence_words(string)
    for key, val in DictTFIDF.items():
        if key in DictIDF:
            DictTFIDF[key] = val * DictIDF[key]
        else:
            DictTFIDF[key] = 0
    return DictTFIDF


def tfidf_matrix_of(string):
    DictTFIDF = dict_score_TFIDF_question(string)
    tfidfTuple = ([], [])
    for key, val in DictTFIDF.items():
        tfidfTuple[0].append(key)
        tfidfTuple[1].append(val)
    tfidfMatrix = []
    for element in tfidfTuple:
        tfidfMatrix.append(element)
    return tfidfMatrix