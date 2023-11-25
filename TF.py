# fonction dont le parametre est chaine de chr qui retourne un dictionnaire {nombreOccurence : mot}

"""
    Fonction qui retourne un dictionnaire dont la clé est le mot et sa valeur est le nombre d'occurence pour chaque fichier
    :param: une chaine de caractere ( elle represente tout le contenu du fichier apres nettoyage )
    :return: dictionnaire {mot : nbOccurence}
    :rtype: dictionnaire
    """
def CalculateOccurenceWords(string):
    nb_occurence = {}
    words = string.split()
    for word in words:
        if word not in nb_occurence:
            nb_occurence[word] = 1
        else:
            nb_occurence[word] += 1
    return nb_occurence
