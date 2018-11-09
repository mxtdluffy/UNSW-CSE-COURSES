
from collections import defaultdict, deque
import sys


'''
Computes all transformations from a word word_1 to a word word_2, consisting of
sequences of words of minimal length, starting with word_1, ending in word_2,
and such that two consecutive words in the sequence differ by at most one letter.
All words have to occur in a dictionary with name dictionary.txt, stored in the
working directory.
'''


dictionary_file = 'dictionary.txt'
dictionary = []
with open(dictionary_file) as open_file:
    for each_line in open_file:
        dictionary.append(each_line[:-1])


def word_ladder(word_1, word_2):
    # lexicon, closest_words = get_words_and_word_relationships()
    # Complete this function
    word_1 = word_1.upper()
    word_2 = word_2.upper()
    if len(word_1) != len(word_2):
        return []
    if word_1 == word_2:
        return [[word_1]]
    find_ladder = dict()
    length = len(word_1)
    same_length = []
    for word in dictionary:
        if len(word) == len(word_1):
            find_ladder[word] = []
            same_length.append(word)
    
    for key in find_ladder:
        for word in same_length:
            for i in range(length):
                new_key = list(key)
                new_word = list(word)               
                new_key[i] = ''
                new_word[i] = ''
                if new_key == new_word and key != word:
                    find_ladder[key].append(word)
    solutions = []
    queue = deque([[word_1]])
    while queue:
        word_sequence = queue.pop()
        last_word = word_sequence[-1]
        for word in find_ladder[last_word]:
            if word == word_2:
                if not solutions or len(solutions[-1]) > len(word_sequence):
                    solutions.append(word_sequence + [word])
            if not solutions and word not in word_sequence:
                queue.appendleft(word_sequence + [word])
    return solutions


                    
            
