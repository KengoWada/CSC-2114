#!/usr/bin/python

"""
PSET2 - Getting familiar with different aspects of python 
(If you get difficulty doing these numbers refer to the online reference
http://software-carpentry.org/v4/python/)

Instructions:
Complete the following functions and test them with the code in the comments
You know you have gotten them right if there are no errors

Submit this file and the rest in a zip to the dropbox on the elearning platform

If you want to test your solutions you can create another file and import this file
and run your new file with "python new_file.py" Example file is :
-------------------
from python_functions import *

print_and_add_odd_numbers(5)

------------------

Name: Kengo Wada
Student Number: 217015747
Email: louiskengo3@gmail.com
"""

def print_and_add_n_odd_numbers(N):

    """
    Print out the first N odd numbers and sum them up
    Return the printed numbers and the sum
    Hint: Consider calculating the modulus
    E.g. 
        sum5nums = print_and_add_n_odd_numbers(5)
        1 3 5 7 9
        sum5nums = 25
    """

    #<write your code here>
    total = 0
    numbers = range(1, N * 2, 2)

    for number in numbers:
        total += number
        print(number)    
    return 'Sum = {}'.format(total)


new = print_and_add_n_odd_numbers(5)
print(new)

def print_triangle_with_base_N(N):
    
    """
    Print out a triagle of * with base of N '*'S
    Hint: Consider using a loop e.g. a while loop
    E.g. 
        print_triangle_with_base_N(4)
        *
        **
        ***
        ****
    """
    #<write your code here>
    for i in range(N, 0, -1):
        print((N+1-i)*'*')
        
        
def readfile_and_change_letters(filename):
    
    """
    Read in a text file line by line and for each line format
    the line to have the first letter at the end of the word, also append
    the letters "ay" at the end.
    Function prints out each word on a line and the modified version
    Hint: Google on how to read text files in python, consider using the 
        line.strip() command and the format() command of the print function
    E.g. 
        readfile_and_change_letters('words.txt')
        hello : ellohay
        there : heretay
        where : hereway
    """
    # <write your code here>
    data = open(filename, 'r+')
    for line in data:
        new = list(line.strip())
        new.append(new.pop(0))
        new.append('ay')
        new_line = ''.join(new)
        print(new_line)
    data.close()

    
def earlier_string(first_str, second_str, string_dict):
    
    """
    Read in two strings and a dictionary and return either first_str
    or second_str; the string with the smallest value
    Hint: Google on using dictionaries in python
    E.g. 
        earlier_string('c', 'b', {'a':1, 'b':3, 'c':4})
        'b'
    """
    #<write your code here>
    one = string_dict[first_str]
    two = string_dict[second_str]

    if one < two:
        return first_str
    else:
        return second_str
        
def dna_2_num(dnastring):
    """
    Consider DNA with the strands 'A','C','G','T'] 
    This function takes a string of DNA and returns a string of numbers that       
    correspond to the value of the strands in the string. It also returns 
    the sum of these numbers. Use the dnakey dictionary to map the strands
    to the numbers.
    Hint: Google on using dictionaries in python
    E.g. 
        dnastring, dnasum = dna_2_num('ACCTTGCCAAAATTGC')
        dnastring = '2335543322225543'
        dnasum = 53
    """
    #<write your code here>
    dna_dictionary = {'A': 2, 'C':3, 'G':4, 'T':5}
    new_list  = []
    dnasum = 0
    for letter in dnastring:
        new_list.append(str(dna_dictionary[letter]))
        dnasum += dna_dictionary[letter]
    owaye = ''.join(new_list)
    print('DNAString = {}').format(owaye)
    print('DNA_Sum = {}').format(dnasum)
