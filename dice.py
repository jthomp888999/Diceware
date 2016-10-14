#!/usr/bin/env python2.7

#####################################################################
# TODO:                                                             #
#   Create options for different output formats of password, i.e.:  #
#                                      special chars                #
#                                      replace letters with numbers #
#####################################################################

from random import SystemRandom
from pyperclip import copy
import sys
import argparse
import dice_dict as d1
import dice_dict2 as d2

# creates a random where each digit is between 1 and 6 joins into one number
def rand_Key():
    crypt = SystemRandom()
    key = [crypt.randrange(1,7) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# matches and yields generated words
def word_return(n_of_Words, d_to_use):
    count = 1
    while count <= n_of_Words:
        count += 1
        key = rand_Key()
        word = d_to_use.dice[key]
        yield word

# Takes yielded pass word and uses join to create different outputs
def morph_pass(words, arg):
    passlist = []
    for word in words:
        passlist.append(word)
    if arg == 'hyphen':
        result = '-'.join(passlist)
    elif arg == 'underscore':
        result = '_'.join(passlist)
    elif arg == 'space':
        result = ' '.join(passlist)
    elif arg == '':
        result = ''.join(passlist)
    return result


# Handle arguments and options
def main():
    opt = argparse.ArgumentParser(
        description='Create A password from a virtual diceroll',
        usage='%(prog)s [-h] -w --words [-d --dictionary] [-m --morph] [-c --copy]')

    opt.add_argument(
        '-w','--words',
        type=int,
        help='Number of words to create',
        metavar='',
        required=True)

    opt.add_argument(
        '-d','--dictionary',
        choices=['eff', 'original'],
        help='Dictionary to use, eff or original',
        metavar='',
        default='original')

    opt.add_argument(
        '-m','--morph',
        choices=['hyphen', 'underscore', 'space'],
        help='Add space, hyphen, or underscore between words.',
        default='',
        metavar='')

    opt.add_argument(
        '-c','--copy',
        help='Copy to clipboard instead of printing',
        action='store_true')

    arg = opt.parse_args()
    n_of_Words = arg.words
    d = arg.dictionary
    morph = arg.morph


    if d == 'eff':
        d_to_use = d1
    if d == 'original':
        d_to_use = d2

    words = word_return(n_of_Words, d_to_use)
    final = morph_pass(words, morph)

    if arg.copy:
        copy(final)
    else:
        sys.stdout.write(final)

if __name__ == '__main__':
    main()