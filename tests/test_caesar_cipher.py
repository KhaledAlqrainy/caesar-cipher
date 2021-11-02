from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack
import pytest


def test_version():
    assert __version__ == '0.1.0'


string = 'a glittering gem is not enough'
string2 = 'the best key lime pie is still up for debate'

def test_encrypt():
    
    actual = encrypt(string, 2)
    expect = 'c inkvvgtkpi igo ku pqv gpqwij'
    assert actual == expect

    actual2 = encrypt(string2, 25)
    expect2 = 'sgd adrs jdx khld ohd hr rshkk to enq cdazsd'
    assert actual2 == expect2


def test_decrypt():
    encrypted1 = encrypt(string, 11)
    encrypted2 = encrypt(string2, 5)

    actual1 = decrypt(encrypted1, 11)
    expect1 = string
    assert actual1 == expect1

    actual2 = decrypt(encrypted2, 8)
    not_expect2 = string2
    assert actual2 != not_expect2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Gd chcm's gddc sgd vzqmhmf zmc hs gzc stqmdc nts rtqoqhrhmfkx vdkk","He didn't heed the warning and it had turned out surprisingly well"),
        ("Vjg umgngvqp jcf umgngvqpu qh jku qyp kp vjg enqugv","The skeleton had skeletons of his own in the closet"),
        ("Xas qsvi hecw erh epp lmw tvsfpiqw asyph fi wspzih","Two more days and all his problems would be solved")
    ],
)
def test_crack(test_input, expected):
    actual = crack(test_input)
    assert actual == expected


def test_best_worst_time_phrase():
    phrase = 'It was the best of times, it was the worst of times.'
    encrypted = encrypt(phrase, 44)
    actual = crack(encrypted)
    expect = phrase
    assert actual == expect