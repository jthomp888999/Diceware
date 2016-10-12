#!/usr/bin/env python2.7

from random import randint
import sys
# imports separate dictionary file
import dice_dict as d
#####################################################################
# TODO:                                                             #
#   Use better RNG                                                  #
#   Incorporate argparse                                            #
#   Create options for copying to clipboard                         #
#   Create options for different output formats of password, i.e.:  #
#                                      special chars                #
#                                      replace numbers with letters #
#   Maybe incorporate different word-list                           #
#####################################################################

def usage():
    sys.stdout.write('Usage:\n\t'+sys.argv[0]+' [#]\n')
    sys.stdout.write('\t#\tNumber of words to generate in password')

# creates a random where each digit is between 1 and 6 joins into one number
def rand_Key():
    key = [randint(1,6) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# matches and yields generated words
def word_return(n_of_Words):
    try:
        count = 1
        while count <= n_of_Words:
            count += 1
            key = rand_Key()
            word = d.dice[key]
            yield word
    except KeyboardInterrupt:
        sys.exit()

# Just get argv[1] and run the functions above
def main():
    sys.stdout.write('http://world.std.com/~reinhold/diceware.html\n\n')
    try:
        n_of_Words = int(sys.argv[1])
        words = word_return(n_of_Words)
        for word in words:
            sys.stdout.write(word.title())
    except ValueError:
        usage()
        sys.exit()
    except IndexError:
        usage()
        sys.exit()

if __name__ == '__main__':
    main()