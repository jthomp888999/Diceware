#!/usr/bin/env python2.7

#####################################################################
# TODO:                                                             #
#   Create options for different output formats of password, i.e.:  #
#                                      special chars                #
#                                      replace letters with numbers #
#   Maybe incorporate different word-lists                          #
#####################################################################

from random import SystemRandom
from pyperclip import copy
import sys
import argparse
# imports separate dictionary file
import dice_dict as d

def usage():
    sys.stdout.write('Usage:\n\t'+sys.argv[0]+' [#]\n')
    sys.stdout.write('\t#\tNumber of words to generate in password')

# creates a random where each digit is between 1 and 6 joins into one number
def rand_Key():
    crypt = SystemRandom()
    key = [crypt.randrange(1,6) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# matches and yields generated words
def word_return(n_of_Words):
    count = 1
    while count <= n_of_Words:
        count += 1
        key = rand_Key()
        word = d.dice[key]
        yield word

# Handle arguments and options
def main():
    opt = argparse.ArgumentParser(
        description='Create A password from a virtual diceroll',
        usage='%(prog)s [-h] [-w --words]')

    opt.add_argument(
        '-w','--words',
        type=int,
        help='Number of words to create',
        metavar='',
        required=True)

    arg = opt.parse_args()
    n_of_Words = arg.words
    words = word_return(n_of_Words)

    for word in words:
        sys.stdout.write(word.title())

if __name__ == '__main__':
    main()