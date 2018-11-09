# Written by Jingyun Shen for COMP9021 Lab_1

"""
This program prompts the user for a strictly positive
integer, nb_of_elements, generates a list of nb_of_elements
random integers between - 50 and 50, prints out the list,
computes the mean, the median and the standard deviation
in two ways, that is, using or not the functions from the
statistics module, and prints them out. 
"""

from random import seed, randint
from numpy import mean, median, std
from math import sqrt
import sys


def find_mean(L):
    sum_L = 0
    for i in range(len(L)):
        sum_L += L[i]
    mean = sum_L / len(L)
    return mean

def find_median(L):
    L.sort()
    median = (L[int(len(L) / 2 - 1)] + L[int(len(L) / 2)]) / 2 \
                     if len(L) % 2 == 0 else L[int(len(L) / 2)]
    return median

def find_standard_deviation(L):
    mean = find_mean(L)
    var = 0
    for i in range(len(L)):
        var += (L[i] - mean) ** 2
    standard_deviation = sqrt(var / len(L))
    return standard_deviation

def main():
    # Prompts the user for a seed for the random number generator,  
    # and for a strictly positive number, nb_of_elements.def main():
    try:
        arg_for_seed = int(input('Input a seed for the random number generator: '))
    except ValueError:
        print('Input is not an integer, giving up.')
        sys.exit()   
    try:
        nb_of_elements = int(input('How many elements do you want to generate? '))
    except ValueError:
        print('Input is not an integer, giving up.')
        sys.exit()
    if nb_of_elements <= 0:
        print('Input should be strictly positive, giving up.')
        sys.exit()
        
    # Generates a list of nb_of_elements random integers between 0 and 99.
    seed(arg_for_seed)
    L = [randint(-50, 50) for _ in range(nb_of_elements)]
    
    # Prints out the list, computes the difference between the largest
    # and smallest values in  the list, and prints it out.
    print('\nThe list is:', L)
    print(f'\nThe mean is: {find_mean(L):.2f}')
    print(f'The median is: {find_median(L):.2f}')
    print(f'The standard deviation is: {find_standard_deviation(L):.2f}')
    print('\nConfirming with functions from the statistics module:')
    print(f'The mean is: {mean(L):.2f}')
    print(f'The median is: {median(L):.2f}')
    print(f'The standard deviation is: {std(L):.2f}')
    return 0

if __name__ == '__main__':
    main()
