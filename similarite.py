from words_classifier import tfidf_matrice
from math import sqrt

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
    

def scalar_product(matrix_words_and_doc_lines, matrix_question):
    scalar_product = 0
    for i in range(len(matrix_question[0])):
        if matrix_question[0][i] in matrix_words_and_doc_lines [0]:
            scalar_product += matrix_question[1][i] * matrix_words_and_doc_lines[1][matrix_words_and_doc_lines[0].index(matrix_question[0][i])]
    return scalar_product

def norm(matrix_line):
    norm = 0
    for i in range(len(matrix_line)):
        if type(matrix_line[i]) != "str" and matrix_line[i] != 0 :
            norm += matrix_line[i]**2
    return sqrt(norm)

def similarity(matrix_words_and_doc_lines, matrix_question):
    return scalar_product(matrix_words_and_doc_lines, matrix_question) / (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1]))

#print(scalar_product(transpose_this(tfidf_matrice())[0:2],[['france', 'inquiétude', 'gouvernemental', 'imaginer'],[1,1,1,1]]))
print(similarity(transpose_this(tfidf_matrice())[0:2],[['france', 'inquiétude', 'gouvernemental', 'imaginer'],[1,1,1,1]]))
