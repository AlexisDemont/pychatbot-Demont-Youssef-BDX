from speechesCleaner import speechesCleaner
from TfIdf import TfIdf_Matrice
"""
    Fonction qui retourne une matrice TF-IDF après le nettoyage des texte
    :param: répertoire à determiner
    :return: matrice TF-IDF dont les lignes representent les mots avec chacun son score TF-IDF dans chaque fichier en colonne
    :rtype: matrice 
    """
def launchFileProcessingAndTFIDF(directory):
    speechesCleaner()
    return TfIdf_Matrice()

