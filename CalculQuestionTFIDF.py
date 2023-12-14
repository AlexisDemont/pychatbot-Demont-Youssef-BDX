from utils import calculate_occurence_words
from utils import calculate_idf
from x import fct1
def ScoreTfQuestion(string):

    TF = calculate_occurence_words(string)

    for key , val in TF.items():
        TF[key] = val/len(fct1)
    return TF

def ScoreTFIdfQuestion (string , directory) :


    list_files = list_of_files(directory, '.txt')
    matrice = [[files.replace('_cleaned', '') for files in list_files]]
    matrice[0].insert(0, '')
    idf = calculate_idf("./cleaned", ".txt")
    all_words = set().union(*create_file_words_dict().values())
    files_tf = {file: ScoreTfQuestion(string)}
    for word in all_words:
        line = [word]
        for file in list_files:
            tf = files_tf[file]
            if word not in tf:
                tf[word] = 0
            line.append(tf[word] * idf[word])
        matrice.append(line)
    return matrice
# verifier si c'est bon
