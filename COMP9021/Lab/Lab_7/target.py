
from random import choice, sample
from collections import defaultdict

class Target:
    '''
    Generates a target, that is, a 3 x 3 grid of distinct letters
    such that at least one 9-letter word is made from all letters in the target.
    The aim of the puzzle is to find words consisting of distinct letters all in the target,
    one of which has to be the letter at the centre of the target.

    To create a target object, three keyword only arguments can be provided:
    - dictionary, meant to be the file name of a dictionary storing all valid words,
      with a default value named dictionary.txt, for a default dictionary supposed to be stored
      in the working directory;
    - target, with a default value of None, otherwise meant to be a 9-letter string defining
      a valid target (in case it is not valid, it will be ignored and a random target will be
      generated as if that argument had not been provided);
    - minimal_length, for the minimal length of words to discover, with a default value of 4.
    '''
    def __init__(self, *, dictionary = 'dictionary.txt', target = None, minimal_length = 4):
        self.dictionary = dictionary
        self.target = target
        self.minimal_length = minimal_length
        with open(self.dictionary) as lexicon:
            self.words = dict(filter(lambda x: len(x[0]) == len(x[1]), ((word, set(word))
                                                     for word in (line.rstrip() for line in lexicon)
                                                                       )
                                    )
                             )
        self.target_letters = []
        for word in self.words:
            if len(word) == 9:
                self.target_letters.append(self.words[word])
        if target:
            self.target_letters = set(target)
            

    def __str__(self):
        target = ''
        for i in range(9):
            if i % 3 == 0:
                target += f'\n       ___________\n\n      | {self.target[i]} |'
            else:
                target += f' {self.target[i]} |'
        target += '\n       ___________\n'
        return target
        
    def __repr__(self):
        return f'Target(dictionary = {self.dictionary}, minimal_length = {self.minimal_length})'     
        
    def number_of_solutions(self):
        pass
        # Replace pass above with your code
        
    def give_solutions(self, minimal_length = None):
        '''
        By default, all solutions are displayed, unless minimal_length is passed as an argument,
        in which case only solutions of length at least that value are displayed.
        '''
        pass
        # Replace pass above with your code

    def change_target(self, to_be_replaced, to_replace):
        '''
        Both arguments are meant to be strings.
        The target will be modified if:
        - to_be_replaced and to_replace are different strings of the same length;
        - all letters in to_be_replaced are distinct and occur in the current target;
        - replacing each letter in to_be_replaced by the corresponding letter in to_replace
          yields a valid target.
        If those conditions are not satisfied then the method prints out a message indicating
        that the target was not changed.
        If the target was changed but consists of the same letters, and with the same letter
        at the centre, then the method prints out a message indicating that the solutions
        are not changed.
        '''
        pass
        # Replace pass above with your code

    # Possibly define helper methods.
