import string

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

'''
    Removes stop words from given text
    (i'm assuming if we were to use this it'd be on strings only?
    i.e with query or doc should already be opened)

    text - string of text to remove from 
    stop_words - global var holding stop words from NLTK library

    Returns: a sentence in string representation without stop words
'''
try:
    stop_words = set(stopwords.words('english'))
except:
    pass


def remove_stopword(text):
    try:
        text = text.translate(None, string.punctuation)
        tokens = word_tokenize(text)
        filtered_text = [word for word in tokens if not word in stop_words]
        return " ".join(filtered_text)
    except:
        return None


'''
    Reduces words down to stems
    (i made two versions, one taking a doc/file and one taking plain text)
    (then i thought about it and maybe we only need the text version)

    text - string of text to stem
    doc - document to stem

    uses Porter Stemming - gives the root of the word, might give non-english words (destabilize -> destabil),
                      but gives good variety of different versions of a word so not too aggressive
'''

porter = PorterStemmer()


def stem_text(text):
    try:
        text = text.translate(None, string.punctuation)
        tokens = word_tokenize(text)
        stemmed_text = []

        for token in tokens:
            stemmed_text.append(porter.stem(token))

        return " ".join(stemmed_text)
    except:
        return None


def stem_doc(doc):
    try:
        content = open(doc, mode="r")
        lines = content.readlines()
        stemmed_doc = []

        for line in lines:
            stemmed_doc.append(stem_text(line))

        return " ".join(stemmed_doc)
    except:
        return None


# an example hahe
# input = 'The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. Ding  A single lap should be completed each time you hear this sound. Ding  Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, ding'
#
# print('Original:\n' + input + '\n')
# print('Removing Stop Words:\n' + remove_stopword(input) + '\n')
# print('Stemming:\n' + stem_text(input))
