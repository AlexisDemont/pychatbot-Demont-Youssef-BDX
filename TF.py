# fonction dont le parametre est chaine de chr qui retourne un dictionnaire {nombreOccurence : mot}
def TF ( string ):
    # Liste de tous les mots du texte ( il y a des mots qui sont répétés)
    words =  string.split()
    # nombre d'occurence de chaque mot de la liste et l'ajouter au dictionnaire { nbOccurence : mot }
    nb_occurence = {}
    for i in range (len(words)):
        if words[i] != "" :
            n = 1
            for j in range (i+1,len(words)):
                if words[i] == words[j] :
                    n += 1
                    print("test" , words[j])
                    words[j] = ""
            word = words[i]
            nb_occurence[word] = n
        print(nb_occurence)

TF("Je suis une patate patate")