def scalar_product(matrix_words_and_doc_lines, matrix_question):
    """
    Function that calculates the scalar product of two matrices

    Parameters:
        matrix_words_and_doc_lines (list): Matrix of a document
        matrix_question (list): Matrix of a question

    Returns:
        scalar_product (int): Scalar product of the two matrices
    """
    scalar_product = 0
    for i in range(len(matrix_question[0])):
        if matrix_question[0][i] in matrix_words_and_doc_lines[0]:
            scalar_product += (
                matrix_question[1][i]
                * matrix_words_and_doc_lines[1][
                    matrix_words_and_doc_lines[0].index(matrix_question[0][i])
                ]
            )
    return scalar_product


def norm(matrix_line):
    """
    Function that calculates the norm of a matrix line

    Parameters:
        matrix_line (list): Input matrix line

    Returns:
        norm (float): Norm of the matrix line
    """
    from math import sqrt

    norm = 0
    for i in range(len(matrix_line)):
        if type(matrix_line[i]) != "str" and matrix_line[i] != 0:
            norm += matrix_line[i] ** 2
    return sqrt(norm)


def similarity(matrix_words_and_doc_lines, matrix_question):
    """
    Function that calculates the cosine similarity between two matrices

    Parameters:
        matrix_words_and_doc_lines (list): Matrix of a document
        matrix_question (list): Matrix of a question

    Returns:
        cosine_similarity (float): Cosine similarity between the two matrices
    """
    if (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1])) == 0:
        return 0
    return scalar_product(matrix_words_and_doc_lines, matrix_question) / (
        norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1])
    )


def most_pertinent_doc(matrix, matrix_question):
    """
    Function that finds the most pertinent document based on the cosine similarity score

    Parameters:
        matrix (list): Matrix of a document
        matrix_question (list): Matrix of a question

    Returns:
        most_pertinent_doc (str): Most pertinent document based on the cosine similarity score
    """
    most_pertinent_doc = ""
    most_pertinent_doc_score = 0
    for i in range(1, len(matrix)):
        score = similarity(matrix[0 : i + 1 : i], matrix_question)
        if score > most_pertinent_doc_score:
            most_pertinent_doc_score = score
            most_pertinent_doc = matrix[i][0]
    if most_pertinent_doc_score == 0:
        return False
    return most_pertinent_doc


def most_pertinent_word_related_to_doc(matrix_question, doc):
    """
    Function that finds the most pertinent word related to a document

    Parameters:
        matrix_question(list): tf-idf of the question
        doc (str): Most pertinent document

    Returns:
        most_pertinent_word (str): Most pertinent word related to the document
    """
    from utils import create_file_words_dict
    from words_classifier import not_important_word

    non_pertinent_words = not_important_word("./cleaned/")
    words = create_file_words_dict("./cleaned/")[
        doc.split(".")[0] + "_cleaned." + doc.split(".")[1]
    ]
    most_pertinent_word = False
    most_pertinent_word_score = 0
    for i in range(len(matrix_question[0])):
        if (
            matrix_question[1][i] > most_pertinent_word_score
            and matrix_question[0][i] in words
            and matrix_question[0][i] not in non_pertinent_words
        ):
            most_pertinent_word_score = matrix_question[1][i]
            most_pertinent_word = matrix_question[0][i]
    return most_pertinent_word


def extract_answer(doc, word):
    """
    Function that extracts the first phrase containing a word in a document

    Parameters:
        word (str): A word
        doc str): A document

    Returns:
        answer (str): Extracted answer
    """
    from utils import file_reader
    from text_organization import string_cleaner

    doc = file_reader(doc, "./speeches/")
    for ele in doc.split("."):
        temp = string_cleaner(ele)
        for words in temp.split(" "):
            if word == words.lower():
                return ele.rstrip() + "."
    return False


def humanize_answer(question, answer):
    """
    Function that improve the answer to make it more 'human'

    Parameters:
        question (str): A question
        answer (str): An answer to the question
    Returns:
        answer (str): Humanized answer
    """
    from random import randint

    question_starters = {
        "Comment": ["Après analyse, ", "Après réflexion, ", "Après étude, "],
        "Pourquoi": ["Car, ", "Parce que, ", "Puisque, ", "Vu que, "],
        "Peux-tu": [
            "Oui, bien sûr!",
            "Évidemment!",
            "Bien sûr!",
            "Oui!",
            "Tout à fait!",
        ],
        "Qui": ["Et bien, "],
    }
    for ele in question_starters.keys():
        if ele.lower() == question.split()[0].lower():
            random = randint(0, len(question_starters[ele]) - 1)
            answer = answer[1].lower() + answer[2:]
            answer = question_starters[ele][random] + answer
            return answer
    return answer


def generate_answer_to_this(question):
    """
    Function that generates an answer to a given question

    Parameters:
        question (str): Input question

    Returns:
        humanize_answer() (str): Generated answer
    """
    from words_classifier import search_common_words, tfidf_matrice
    from utils import transpose_this
    from text_organization import tfidf_matrix_of

    transposed_matrix = transpose_this(tfidf_matrice())
    tf_idf_question = tfidf_matrix_of(search_common_words(question, "./cleaned/"))
    pertinent_doc = most_pertinent_doc(transposed_matrix, tf_idf_question)
    if not pertinent_doc:
        return "There is no pertinent answer to this question in the corpus."
    pertinent_word = most_pertinent_word_related_to_doc(tf_idf_question, pertinent_doc)
    answer = extract_answer(pertinent_doc, pertinent_word)
    if not answer:
        return "There is no pertinent answer to this question in the corpus."
    return humanize_answer(question, answer)
