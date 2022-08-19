# The chooser.
import random as ra

def chooser(num: int, only: bool=False, *names):
    '''Quickly select num elements from the names.
    Optional - only: Does not repeat the element, 
    but reduces the number of elements returned.'''
    results = []
    for n in range(num):
        result = ra.choice(names)
        results.append(result)
    if only == True:
        return list(set(results))
    return results