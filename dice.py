#!/usr/bin/env python2.7

from random import randint
import sys

# https://stackoverflow.com/questions/4803999/python-file-to-dictionary
def get_pair(line):
  key, sep, value = line.strip().partition(" ")
  return int(key), value

# takes a word list and runs get_pair on it then converts that to a dictionary
def fileToDict(wordlist):
    with open(wordlist) as fd:
        d = dict(get_pair(line) for line in fd)
        return d

# just creates a random where each digit is between 1 and 6
# joins into one number
# as of now not using the best prng
# https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
def randKey():
    key = [randint(1,6) for p in range(0,5)]
    keyInt = ''.join(map(str,key))
    return int(keyInt)

# takes the random key from above and returns the matching word from the dictionary
def diceWord():
    key = randKey()
    diceDict = fileToDict('wordlist.txt')
    word = diceDict[key]
    return word.title()

# main loop that should print the random word matched from the dictionary for as many words as requested
def main():
    nOfWords = int(sys.argv[1])
    count = 1
    try:
        while count <= nOfWords:
            count += 1
            word = diceWord()
            # use sys.stdout to print all on the same line
            sys.stdout.write(word+'_')
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()