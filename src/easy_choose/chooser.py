# The chooser.
import random as ra

def chooser(num: int, only: bool, *names):
    '''The chooser.'''
    results = []
    for n in range(num):
        result = ra.choice(names)
        results.append(result)
    if only == True:
        return list(set(results))
    return results