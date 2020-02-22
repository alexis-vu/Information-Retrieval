import sys
from PartA import tokenize

'''
PROGRAM

Tokenize Each File and Turn Into Set (to remove duplicates for faster processing): O(mn)
    -> O(nm): tokenizing the file (comuputed in PartA),
              m = # words per line, n = # lines in file
    -> O(n): turning returned list into set,
             n = # tokens in the token list


Take Length of Intersection of Sets: O(min(len(token_list1), token_list2))
    -> O(min(len(token_list1), token_list2)): taking intersection, according to wiki.python.org

    -> O(1): getting length of intersection

Worst Case: O(mn + min(len(token_list1), token_list2)) = O(nm)
'''
def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    token_list1 = set(tokenize(file1))
    token_list2 = set(tokenize(file2))

    print(len(token_list1 & token_list2))

if __name__ == "__main__":
  main()
