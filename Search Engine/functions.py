import math
import json
import word_func

doc_length = open("doc_length.txt", "r")
doc_length_dict = json.loads(doc_length.read())

terms = open("terms.txt", "r")
terms_dict = json.loads(terms.read())


def parse(text):
    tokens = []
    length = len(text)
    char = 0

    while char < length:
        if text[char] == '<':
            while char < length and text[char] != '>':
                char += 1
        else:
            while char < length and text[char] == ' ':
               char += 1

            start = char

            # 0-9,A-Z,a-z

            while char < length and ( (ord(text[char]) > 47 and ord(text[char]) < 58) or (ord(text[char]) > 64 and ord(text[char]) < 91) or (ord(text[char]) > 96 and ord(text[char]) < 123) ):
                char += 1

            temp = text[start:char].lower()
            if len(temp) > 0:
                tokens.append(temp)

            if char < length and text[char] != '<':
                char += 1

    return tokens

# Boolean Retrieval for AND
# pass in the values of the original output (don't need word)
def retrieval_and(doc1, doc2):
    # combined = [doc id : combined frequencies]
    # doc = dict[doc id : frequency]

    combined = dict()
    doc1_s = set(doc1.keys())
    doc2_s = set(doc2.keys())
    doc_ids = doc1_s.intersection(doc2_s)

    for doc in doc_ids:
        combined[doc] = doc1[doc] + doc2[doc]

    return combined

# with open('name.json', 'r') as file:
#     text = json.loads(file.read())['content']

#     print(parse(text))

# <a>fadsfkjldskljfds</a>fsdhjklsdf

# creates a query tf-idf to use for cosine similarity
def query_tf_idf(query):

        query_tf_idf_dict = {}
        docs = len(doc_length_dict.keys())
        for n in query:
            try:
                q_tf = (query.count(n)/(len(query)))
                q_idf = 1 + math.log(docs/len(terms_dict[n].keys()))
                query_tf_idf_dict[n] = (q_tf*q_idf)
            except(KeyError):
                pass
        return query_tf_idf_dict



# Creates a tf-idf for each token in every document
# tf-idf is also normalized to calculate cosine similarity
def tf_idf_weight():
    tf_idf = {}
    docs = len(doc_length_dict.keys())

    for token in terms_dict:
        doc_frequency = len(terms_dict[token].keys())
        tf_idf[token] = {}
        for doc in terms_dict[token]:
            tf = terms_dict[token][doc] / doc_length_dict[doc]
            idf = 1 + math.log(docs/doc_frequency)
            tf_idf[token][doc] = (tf*idf)
    return tf_idf

tf_idf_dict = tf_idf_weight()


def cosine_similarity(query, doc):
    doc_product = float(0)
    query_vector = float(0)
    doc_vector = float(0)

    # n = term
    for n in query.keys():
        doc_product += float(query[n]*tf_idf_dict[n][doc])
        query_vector += float((query[n])**2)
        doc_vector += float((tf_idf_dict[n][doc])**2)

    return doc_product/(math.sqrt(query_vector)*math.sqrt(doc_vector))

def doc_score(query, doc):
    score = 0
    for n in query:
        if doc in tf_idf_dict[n].keys():
            score += tf_idf_dict[n][doc]
    return score


def query_without_stopwords(query):
    return word_func.remove_stopword(query)

def query_stemming(query):
    return word_func.stem_text(query)
