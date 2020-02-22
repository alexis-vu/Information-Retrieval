import re

'''
TOKENIZE

Opening File & Reading In Lines: O(n)
    -> O(n): filling list with each line, n = # lines of input file

Process Each Line and Tokenize: O(n * (m + m)) = O(nm)
    -> O(n * m): O(1) for stripping whitespace in front/end of line
               + O(m) for adding each alphanumeric token in the line to a list,
                      m = # words in a line,
               n = # lines in line list

    -> O(m): O(1) checking if token is empty,
           + O(1) making token lowercase,
           + O(1) adding token to token list,
           m = # tokens in tokenized line

Worst Case: O(n + nm) = O(nm)
'''
def tokenize(file_path):
    with open(file_path) as file_object:
        lines = file_object.readlines()

    tokens = []
    for line in lines:
        line = line.strip()
        split_line = re.split('[^\dA-Za-z]', line)

        for token in split_line:
            if len(token) > 0:
                token = token.lower()
                tokens.append(token)

    return tokens

'''
COMPUTE WORD FREQUENCIES

Process Each Token in Token List: O(n)
    -> O(n): O(1) checking if token already is in token_frequency dictionary,
             n = # tokens in token list

Worst Case: O(n)
'''
def computeWordFrequencies(token_list):
    token_freq = dict()

    for token in token_list:
        if token in token_freq:
            token_freq[token] += 1
        else:
            token_freq[token] = 1

    return token_freq

'''
PRINT FREQUENCIES

Sort Token List by Frequency Count: O(n)
    -> O(n log n): sorting list according to wiki.python.org,
             n = # tokens in token/frequency dictionary

Print Each Token and Its frequency: O(n)
    -> O(n): O(1) access token and token frequency (key,value) pair,
             n = # token/frequency pairs

Worst Case: O(n log n + n) = O(n)
'''
def printFrequencies(token_freq):
    token_freq = sorted(token_freq.items(), key = lambda t: t[1], reverse = True)
    for token in token_freq:
        print("%s -> %d" % (token[0], token[1]))

'''
### TESTING PURPOSES ###
import sys
def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    token_list1 = tokenize(file1)
    token_list2 = tokenize(file2)

    freq1 = computeWordFrequencies(token_list1)
    freq2 = computeWordFrequencies(token_list2)

    print("----------- TOKEN FREQUENCIES: FILE 1 -----------")
    printFrequencies(freq1)

    print("----------- TOKEN FREQUENCIES: FILE 2 -----------")
    printFrequencies(freq2)


if __name__ == "__main__":
        main()
'''
