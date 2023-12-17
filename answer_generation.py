from math import sqrt
from text_organization import tfidf_matrix_of
from words_classifier import tfidf_matrice
from utils import transpose_this
    

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
    if (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1])) == 0:
        return 0
    return scalar_product(matrix_words_and_doc_lines, matrix_question) / (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1]))

def most_pertinent_doc(matrix, matrix_question):
    most_pertinent_doc = ""
    most_pertinent_doc_score = 0
    for i in range(1,len(matrix)):
        score = similarity(matrix[0:i+1:i], matrix_question)
        if score > most_pertinent_doc_score:
            most_pertinent_doc_score = score
            most_pertinent_doc = matrix[i][0]
    if most_pertinent_doc_score == 0:
        return "There is no pertinent document"
    return most_pertinent_doc

print(most_pertinent_doc(transpose_this(tfidf_matrice()), tfidf_matrix_of("quel est le climat ")))

