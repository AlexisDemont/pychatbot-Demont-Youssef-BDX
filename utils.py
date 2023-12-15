import os
from math import log10
from text_organization import string_cleaner

def list_of_files(directory, extension):
    """
    Function that returns a list of file names in the directory with a specific extension
    
    Parameters:
        directory (str): Path to the directory
        extension (str): Extension of the files
        
    Returns:
        files (list): List of file names
        
    """
    return [filename for filename in os.listdir(directory) if filename.endswith(extension)]

def clean_folder(directory='./cleaned', extension='txt'):
    """
    Function that deletes all files in the 'cleaned' directory with a specific extension
    
    Parameters:
        directory (str): Path to the directory of cleaned files
        extension (str): Extension of the files
        
    Returns:
        None
        
    """
    for name in list_of_files(directory, extension):
        os.remove(directory + name)
    return


def file_reader(file, directory):
    """
    Function that reads the content of a file and returns it as a string
    
    Parameters:
        file (str): Name of the file
        directory (str): Path to the directory
        
    Returns:
        content (str): Content of the file as a string
        
    """
    if directory[-1] != '/':
        directory += '/'
    with open(directory+file, 'r') as f:
        return ''.join(f.readlines())
    

    

def calculate_occurence_words(string):
    """
    Function that calculates the occurrence of each word in a string and returns a dictionary
    
    Parameters:
        string (str): Input string
        
    Returns:
        occurences (dict): Dictionary with word as key and occurrence count as value
        
    """
    occurences = {}
    for word in string.split():
        if word not in occurences:
            occurences[word] = 1
        else:
            occurences[word] += 1
    return occurences


def tfidf_matrice(directory='./cleaned/'):
    """
    Function that returns a TF-IDF matrix where each row represents a word and its TF-IDF score in each file (in columns)
    
    Parameters:
        directory (str): Path to the directory of cleaned text files
        
    Returns:
        matrice (list): TF-IDF matrix where each row represents a word and its TF-IDF score in each file (in columns)
        
    """
    list_files = list_of_files(directory, '.txt')
    matrice = [[files.replace('_cleaned', '') for files in list_files]]
    matrice[0].insert(0, '')
    idf = calculate_idf()
    all_words = set().union(*create_file_words_dict().values())
    files_tf = {file: calculate_occurence_words(file_reader(file, directory)) for file in list_files}
    for word in all_words:
        line = [word]
        for file in list_files:
            tf = files_tf[file]
            if word not in tf:
                tf[word] = 0
            line.append(tf[word] * idf[word])
        matrice.append(line)
    return matrice

def transpose_this( matrice ):
    """
      Function that transpose a matrix

      Parameters:
          matrix

      Returns:
          transposed matrix
      """
    rows = len(matrice)
    columns = len(matrice[0])
    transposedMatrice = [[0]*rows for k in range (columns)]
    for i in range (columns):
        for j in range (rows):
            transposedMatrice[i][j] = matrice[j][i]

    return transposedMatrice



def create_file_words_dict(directory="./cleaned/"):
    """
    Function that creates a dictionary where the keys are file names and the values are sets of words in each file
    
    Parameters:
        directory (str): Path to the directory of cleaned text files
        
    Returns:
        file_words (dict): Dictionary where keys are file names and values are sets of words
        
    """
    list_files = list_of_files(directory, ".txt")
    file_words = {}
    for file in list_files:
        words_in_file = set(file_reader(file,directory).split())
        file_words[file] = words_in_file
    return file_words


def calculate_idf(directory="./cleaned/",extension=".txt"):
    """
    Function that calculates the IDF score for each word in all files and returns a dictionary
    
    Parameters:
        directory (str): Path to the directory of cleaned text files
        extension (str): Extension of the files
        
    Returns:
        idf_scores (dict): Dictionary where keys are words and values are IDF scores
        
    """
    file_words=create_file_words_dict(directory)
    list_files = list_of_files(directory, extension)
    all_words = set().union(*file_words.values())
    idf_scores = {}
    for word in all_words:
        word_existence_count = 0
        for file in list_files:
            if word in file_words[file]:  
                word_existence_count += 1
        idf_scores[word] = log10(((len(list_files)) / (word_existence_count)))
    return idf_scores
print(calculate_idf(directory="./cleaned/",extension=".txt"))


def score_TF_question(string):
    """
    Function that calculate the occurence of words in a string

    Parameters:
        string
    Returns:
        dictionary of word : TF
    """
    TF = calculate_occurence_words(string)
    list_of_words = string_cleaner(string)
    # si mot n'est pas dsans matrice alors non
    for key , val in TF.items():
        TF[key] = val/len(list_of_words)

    return TF
print(score_TF_question("le climat Saraah"))
def dict_score_TFIDF_question (string):
    DictIDF = calculate_idf(directory="./cleaned/",extension=".txt")
    DictTFIDF = score_TF_question(string)
    for key , val in DictTFIDF.items():
        if key in DictIDF :
            DictTFIDF[key]= val * DictIDF[key]
    return DictTFIDF
print(dict_score_TFIDF_question("Le climat Sarah"))

def tfidf_matrix_of ( string ):
    DictTFIDF = dict_score_TFIDF_question(string)
    tfidfTuple = ([],[])
    for key , val in DictTFIDF.items():
        tfidfTuple[0].append(key)
        tfidfTuple[1].append(val)
    tfidfMatrix = []
    for element in tfidfTuple:
        tfidfMatrix.append(element)
    return tfidfMatrix
print(tfidf_matrix_of("Le climat Sarah"))

def transpose_this( matrice ):
    """
      Function that transpose a matrix

      Parameters:
          matrix

      Returns:
          transposed matrix
      """
    rows = len(matrice)
    columns = len(matrice[0])
    transposedMatrice = [[0]*rows for k in range (columns)]
    for i in range (columns):
        for j in range (rows):
            transposedMatrice[i][j] = matrice[j][i]

    return transposedMatrice




