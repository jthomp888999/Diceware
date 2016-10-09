#!/usr/bin/env python2.7

from random import randint
import sys
# imports separate dictionary file
import worddict as d

def usage():
    sys.stdout.write('Usage:\n\t' + sys.argv[0] + ' [#]\n')

# creates a random where each
# digit is between 1 and 6
# joins into one number
def randKey():
    key = [randint(1,6) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# main loop that should give the random
# word matched from the dictionary
# for as many words as requested
def main():
    try:
        sys.stdout.write('\n')
        nOfWords = int(sys.argv[1])
        count = 1
        try:
            while count <= nOfWords:
                count += 1
                key = randKey()
                word = d.dice[key]
                sys.stdout.write(word.title())
        except KeyboardInterrupt:
            sys.exit()
        sys.stdout.write('\n')
    except IndexError:
        usage()
        sys.exit()

if __name__ == '__main__':
    main()