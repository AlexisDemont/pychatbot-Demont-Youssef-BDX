# les mots dont le score est eleve
def HighestScore():
    MaxiScores = [] # liste des scores max de chaque mot
    ImportantWords = [] # en parallele les mots correspondants
    for word in matrice : # pour chaque mot (ligne) de la matrice dans tfidf
        ScoreMax = 0
        for ScoreWord in word : # pour chaque score de ce mot dans chaque doc
            if ScoreWord > ScoreMax : # si score superieur au max trouvé alors
                ScoreMax = ScoreWord
        if ScoreMax != 0 :  # si le score max est different de zero donc on le considere important
            MaxiScores.append(ScoreMax)
            ImportantWords.append(word)
    ScoreMax = 0 # comparer les scores pour connaitre le score le + eleve
    for Score in MaxiScores :
        if Score > ScoreMax :
            ScoreMax = Score
    MostImportant = [] # liste de ou des mots dont le score est le max et donc sont importants
    for i in range (len(MaxiScores)):
        if MaxiScores[i] == ScoreMax :
            MostImportant.updates(ImportantWords[i])
    return MostImportant
