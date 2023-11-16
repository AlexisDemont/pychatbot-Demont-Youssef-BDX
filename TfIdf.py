from basicsFunctions import list_of_files, file_reader
from TF import CalculateOccurenceWords
from IDF import CalculateIDF, create_file_words_dict, RegroupAllWords


def TfIdf_Matrice(directory='./cleaned/'):
    list_files = list_of_files('./cleaned', '.txt')
    matrice = [[files.replace('_cleaned', '') for files in list_files]]
    idf = CalculateIDF()
    file_words = create_file_words_dict()
    allWords = RegroupAllWords(file_words)
    files_tf = {file: CalculateOccurenceWords(file_reader(file, directory)) for file in list_files}
    for word in allWords:
        line = [word]
        for file in list_files:
            tf = files_tf[file]  # Use the pre-read file content
            if word not in tf:
                tf[word] = 0
            line.append(tf[word] * idf[word])
        matrice.append(line)
    return matrice