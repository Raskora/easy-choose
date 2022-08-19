# It's just a test here, nothing.

from .chooser import chooser

def testnumbers(number: int=10, num: int=1, only: bool=False):
    '''Num numbers are randomly selected from the number.'''
    numbers = [n for n in range(number+1)]
    return chooser(num, only, *numbers)

def testalphabet_upper(num: int=1, only: bool=False):
    '''Num letters are randomly selected from 26 uppercase letters.'''
    letters = [chr(l) for l in range(65, 91)]
    return chooser(num, only, *letters)

def testalphabet_lower(num: int=1, only: bool=False):
    '''Num letters are randomly selected from 26 lowercase letters.'''
    letters = [chr(l) for l in range(97, 123)]
    return chooser(num, only, *letters)