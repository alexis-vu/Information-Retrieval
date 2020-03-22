import os
import json
from functions import *
from sys import getsizeof

import time

from timeit import timeit

start = timeit()

terms = {}
document = {}
docNum = 0

with open("output.txt", "w") as output:
    for directory in os.listdir('DEV'):
        try:
            print(directory)
            directory = 'DEV/' + directory
            for file in os.listdir(directory):
                document[docNum] = file
                with open(directory + '/' + file, 'r') as file:
                    for word in parse(json.loads(file.read())['content']):
                        try:
                            terms[word]
                            try:
                                terms[word][docNum] += 1
                            except:
                                terms[word][docNum] = 1
                        except:
                            terms[word] = {docNum: 1}
                file.close()
                docNum += 1
        except NotADirectoryError:
            print('not a directory')

    output.write("This is the number of documents there are: " + str(docNum) + '\n')
    output.write("This is the number of unique words there are: " + str(len(terms.keys())) + '\n')


with open('output.txt', 'a') as file:
    file.write(json.dumps(terms))