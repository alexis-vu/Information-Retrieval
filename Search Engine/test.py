import math
terms_dict = {"the": {1:1, 2:1}, "game": {1:2}, "of": {1:2}, "life": {1:1, 2:1, 4:2}, "is": {1:1, 2:1}, "a": {1:1}, "everlasting": {1:1}, "learning": {1:1, 3:1, 4:3}, "unexamined":{2:1}, "not": {2:1, 4:5}, "worth": {2:1, 4:5}, "living": {2:1}, "never": {3:1, 4:5}, "stop": {3:1}}

doc_length_dict = {1: 10, 2:7, 3:3, 4:20}

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

def cosine_similarity(query, doc):
    doc_product = float(0)
    query_vector = float(0)
    doc_vector = float(0)

    # n = term
    for n in query.keys():
        if doc not in tf_idf_dict[n].keys():
            query_vector += float((query[n])**2)
        else:
            doc_product += float(query[n] * tf_idf_dict[n][doc])
            query_vector += float((query[n]) ** 2)
            doc_vector += float((tf_idf_dict[n][doc]) ** 2)

    return doc_product/(math.sqrt(query_vector)*math.sqrt(doc_vector))

def doc_score(query, doc):
    score = 0
    for term in query:
        if doc in tf_idf_dict[term].keys():
            score += tf_idf_dict[term][doc]

    return score

if __name__ == '__main__':
    query = ['life','learning']
    print(tf_idf_dict)

    query_weight = query_tf_idf(query)

    for x in [1,2,3,4]:
        print(cosine_similarity(query_weight, x))

    print("doc scores")
    for x in [1,2,3,4]:
        print(doc_score(query, x))

    print("Combined scores")
    for x in [1,2,3,4]:
        print(cosine_similarity(query_weight, x)+doc_score(query, x))