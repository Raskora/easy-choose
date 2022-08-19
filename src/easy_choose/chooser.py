# The chooser.
import random as ra

def chooser(num: int, *names):
    results = []
    for n in range(num):
        result = ra.choice(names)
        results.append(result)
    return results