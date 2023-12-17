def scalar_product(matrix_words_and_doc_lines, matrix_question):
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
    from math import sqrt

    norm = 0
    for i in range(len(matrix_line)):
        if type(matrix_line[i]) != "str" and matrix_line[i] != 0:
            norm += matrix_line[i] ** 2
    return sqrt(norm)


def similarity(matrix_words_and_doc_lines, matrix_question):
    if (norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1])) == 0:
        return 0
    return scalar_product(matrix_words_and_doc_lines, matrix_question) / (
        norm(matrix_words_and_doc_lines[1][1:]) * norm(matrix_question[1])
    )


def most_pertinent_doc(matrix, matrix_question):
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
    from utils import create_file_words_dict
    from words_classifier import not_important_word

    non_pertinent_words = not_important_word("./cleaned/")
    add_non_pertinent_words = {"quel", "quelle", "quels", "quelles"}
    non_pertinent_words = non_pertinent_words.union(add_non_pertinent_words)
    words = create_file_words_dict("./cleaned/")[
        doc.split(".")[0] + "_cleaned." + doc.split(".")[1]
    ]
    most_pertinent_word = ""
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
    from utils import file_reader
    from text_organization import string_cleaner

    doc = file_reader(doc, "./speeches/")
    for ele in doc.split("."):
        temp = string_cleaner(ele)
        for words in temp.split(" "):
            if word == words.lower():
                return ele + "."
    return False


def generate_answer_to_this(question):
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
    return answer