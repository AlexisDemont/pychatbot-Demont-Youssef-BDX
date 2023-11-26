import os
import re
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
    if '_' in name:
        name = name.split("_")[1]
    if '.' in name:
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
    full_name = 'Anonyme Anonyme'
    for key in dict_names:
        if name in key:
            full_name = str(dict_names[name] + " " + name)
    return str(full_name)


def regroup_text_from_similar_speakers(directory='cleaned',extension='.txt'):
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


def speeches_to_lowercase(directory, extension):
    """
    Function that converts speeches to lowercase

    Parameters:
        directory (str): Path to the directory containing the speeches
        extension (str): Extension of the speech files

    Returns:
        None
    """
    files_names = list_of_files(directory, extension)
    for name in files_names:
        new_name = name.split('.')[0] + '_lowercased.txt'
        with open(directory +'/' + name, 'r') as raw_text, open('./cleaned/' + new_name, 'w') as minimized_text:
            for line in raw_text:
                line = line.lower()
                minimized_text.write(line)
    return


def lowercase_to_clean(directory='./cleaned/', extension='.txt'):
    """
    Function that converts lowercase text to clean text

    Parameters:
        directory (str): Path to the directory containing the lowercase text files
        extension (str): Extension of the lowercase text files

    Returns:
        None
    """
    files_names = list_of_files(directory, extension)
    for name in files_names:
        new_name = name.replace('lowercased', 'cleaned')
        if 'lowercased' in name:
            with open(directory + name, 'r') as lowercased_text, open(directory + new_name, 'w') as cleaned_text:
                for line in lowercased_text:
                    for character in line:
                        if not (character.isalpha()) and not (character.isnumeric()):
                            line = line.replace(character, ' ')
                    line = re.sub(' +', ' ', line)
                    line = line.lstrip()
                    cleaned_text.write(line)
            os.remove(directory + name)
    return


def speeches_cleaner(directory='./speeches/', extension='.txt'):
    """
    Function that converts speeches to lowercase and then them

    Parameters:
        directory (str): Path to the directory containing the lowercase text files
        extension (str): Extension of the lowercase text files

    Returns:
        None
    """
    speeches_to_lowercase(directory, extension)
    lowercase_to_clean()
    return
