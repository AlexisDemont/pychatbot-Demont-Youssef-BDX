#  Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
from president import list_of_names_fillnames
from basicsFunctions import list_of_files, file_reader
from TF import CalculateOccurenceWords
# dictionnaire {president : nbFoisMot}
def SpeakerOfWord (word):
    word = word.lower()
    directory = './cleaned/'
    list_files = list_of_files('./cleaned', '.txt')
    files_tf = {file: CalculateOccurenceWords(file_reader(file, directory)) for file in list_files}
    speaker={}
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


def WordMostSpoken (word):
    speakers = SpeakerOfWord(word)
    maxi = 0
    president=None
    for key in speakers.keys():
        if speakers[key] > maxi :
            maxi = speakers[key]
            president = key
    if president == None:
        return "Aucun président n'a utilisé ce mot"
    return president