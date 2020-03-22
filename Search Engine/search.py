import json
document = open("document.txt", "r")
document_dict = json.loads(document.read())
from functions import retrieval_and, query_tf_idf, cosine_similarity, doc_score

terms = open("terms.txt", "r")
terms_dict = json.loads(terms.read())


def search(search_query):
    search_query = str(search_query)
    terms = search_query.split()
    terms = [x.lower() for x in terms]
    # orders the doc count of each term from smallest to largest
    ordered_terms = sorted(terms, key=lambda x: len(terms_dict[x].keys()))
    final_docs_scores = []

    result = {}
    #creates a set union of the docs that contain all the query terms
    if len(terms) == 1:
        word_dict = terms_dict[ordered_terms[0]]
        for key in word_dict:
            result[key] = word_dict[key]
    if len(terms) == 2:
        result = (retrieval_and(terms_dict[ordered_terms[0]], terms_dict[ordered_terms[1]]))

    elif len(terms) > 2:
        result = (retrieval_and(terms_dict[ordered_terms[0]], terms_dict[ordered_terms[1]]))
        ordered_terms.pop(1)
        ordered_terms.pop(0)
        while len(ordered_terms) >= 1:
            result = (retrieval_and(result, terms_dict[ordered_terms[0]]))
            ordered_terms.pop(0)

    query = query_tf_idf(terms)


    # calculates the cosine similarity results for each of the doc in the set
    for doc in result:
        cosine_score = cosine_similarity(query, doc)
        d_score = doc_score(query.keys(), doc)
        final_docs_scores.append((doc, cosine_score+d_score))



    # returns the top 5

    final_docs_scores.sort(key=lambda x: x[1], reverse=True)

    doc_urls = []

    for x in final_docs_scores:
        print(document_dict[str(x[0])], x[1])
        doc_urls.append(document_dict[str(x[0])])

    return doc_urls
    # if(len(final_docs_scores) < 5):
    #     for x in range(len(final_docs_scores)):
    #         print(document_dict[str(final_docs_scores[x][0])] + " " + str(final_docs_scores[x][1]))
    # else:
    #     for x in range(len(final_docs_scores)):
    #         print(document_dict[str(final_docs_scores[x][0])] + " " + str(final_docs_scores[x][1]))
    #
    # search_query = input("Search for: ")
    # terms = search_query.split()


if __name__ == '__main__':
    search()
