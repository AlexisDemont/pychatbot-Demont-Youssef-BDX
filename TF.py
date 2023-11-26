# fonction dont le parametre est chaine de chr qui retourne un dictionnaire {nombreOccurence : mot}

def extractWordsFromThis(string):
    words = {word for word in string.split()}
    return words

def CalculateOccurenceWords(string):
    """
    Fonction qui retourne un dictionnaire dont la clé est le mot et sa valeur est le nombre d'occurence pour chaque fichier
    :param: une chaine de caractere ( elle represente tout le contenu du fichier apres nettoyage )
    :return: dictionnaire {mot : nbOccurence}
    :rtype: dictionnaire
    """
    nb_occurence = {}
    words = extractWordsFromThis(string)
    for word in words:
        if word not in nb_occurence:
            nb_occurence[word] = 1
        else:
            nb_occurence[word] += 1
    return nb_occurence
