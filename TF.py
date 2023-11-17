# fonction dont le parametre est chaine de chr qui retourne un dictionnaire {nombreOccurence : mot}

def CalculateOccurenceWords(string):
    nb_occurence = {}
    words = string.split()
    for word in words:
        if word not in nb_occurence:
            nb_occurence[word] = 1
        else:
            nb_occurence[word] += 1
    return nb_occurence
