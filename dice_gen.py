#!/usr/bin/env python
import sys
import argparse

# Try to import secrets if available
try:
    from secrets import SystemRandom
except ImportError:
    from random import SystemRandom

# Possible dictionaries to use
import dicts.dice_dict as d1
import dicts.dice_dict2 as d2


# creates a random where each digit is between 1 and 6 joins into one number
def dice_roll():
    key = [SystemRandom().randrange(1, 7) for p in range(0, 5)]
    keyInt = ''.join(map(str, key))
    return int(keyInt)


# matches and yields generated words
def word_return(n_of_Words, d_to_use):
    count = 1
    while count <= n_of_Words:
        count += 1
        yield d_to_use.dice[dice_roll()]


# Takes yielded pass word and uses join to create different outputs
def morph_pass(words, arg):
    passlist = []
    for word in words:
        passlist.append(word)
    return arg.join(passlist)


# Handle all arguments to pass to main
def get_args():
    opt = argparse.ArgumentParser(
        description='Create A password from a virtual diceroll')

    opt.add_argument('num',
                     type=int,
                     nargs='?',
                     default=6,
                     help='Number of words to create, default value is 6')

    opt.add_argument('-d', '--dictionary',
                     choices=['eff', 'original'],
                     help='Dictionary to use, eff or original',
                     metavar='',
                     default='original')

    opt.add_argument('-m', '--morph',
                     help='Choose a character to seperate each word',
                     default='',
                     metavar='')
    return opt


def main():
    # Takes command line options as variables
    arg = get_args().parse_args()

    # Decides which dictionary to use
    if arg.dictionary == 'eff':
        d_to_use = d1
    elif arg.dictionary == 'original':
        d_to_use = d2

    # Finds the word from a dice roll
    words = word_return(arg.num, d_to_use)

    # Returns the result if the password is altered
    final = morph_pass(words, arg.morph)
    sys.stdout.write(final + '\n')

if __name__ == '__main__':
    main()
