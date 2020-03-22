import json
terms = open("terms.txt", "r")
terms_dict = json.loads(terms.read())

doc_length = {}

def load():
    for term in terms_dict:
        for doc in terms_dict[term].keys():
            if doc not in doc_length.keys():
                doc_length[doc] = terms_dict[term][doc]
            else:
                doc_length[doc] += terms_dict[term][doc]

    with open('doc_length.txt', 'a') as file:
        file.write(json.dumps(doc_length))

if __name__ == '__main__':
    load()