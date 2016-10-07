#!/usr/bin/env python2.7

from random import randint
import sys
import worddict as d

# converts given list ('key value' format)
# into the dictionary
# def fileToDict(wordlist):
#     d = {}
#     with open(wordlist) as file:
#         for l in file:
#             key, sep, value = l.strip().partition(" ")
#             key = int(key)
#             d[key] = value
#         return d

# just creates a random where each
# digit is between 1 and 6
# joins into one number as of now
# not using the best prng
def randKey():
    key = [randint(1,6) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# main loop that should print the random
# word matched from the dictionary
# for as many words as requested
def main():
    sys.stdout.write('\n')
    nOfWords = int(sys.argv[1])
    count = 1
    try:
        while count <= nOfWords:
            count += 1
            key = randKey()
            diceDict = d.dice
            word = diceDict[key]
            # use sys.stdout to print all on the same line
            sys.stdout.write(word.title())
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit()
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()