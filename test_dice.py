'''
TODO:
    Test argparse function...
'''

from dice import *
import dice_dict as d1
import dice_dict2 as d2
import types

def test_dicts():
    a = len(d1.dice)
    b = len(d2.dice)
    assert a == 7776
    assert b == 7776

def test_dice_roll():
    test_dice = dice_roll()
    assert len(str(test_dice)) == 5
    assert type(test_dice) == int

def test_word_return_generator():
    is_gen = word_return(11, d2)
    assert isinstance(is_gen, types.GeneratorType)

def test_morph_pass():
    opts = ['hyphen','underscore','space','']
    words = ['this','is','a','test']
    answers = [
    'this-is-a-test','this_is_a_test','this is a test','thisisatest'
    ]
    i = 0
    while i < 4:
        arg = opts[i]
        ans = answers[i]
        test_answer = morph_pass(words, arg)
        assert test_answer == ans
        i += 1
