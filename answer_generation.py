from words_classifier import tfidf_matrice
from math import sqrt
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
    return scalar_product(matrix_words_and_doc_lines, matrix_question) / (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1]))