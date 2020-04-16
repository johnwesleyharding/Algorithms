#!/usr/bin/python

import sys

def making_change(amount, denoms = [1, 5, 10, 25, 50]):
    
    rows = amount // 5 + 1
    cols = len(denoms) - 1

    cache = [[i + 1 for j in range(cols)] for i in range(rows)]

    for i in range(2, rows):

        for j in range(1, len(denoms) - 1):
            
            cache[i][j] = cache[i][j-1]
            
            if denoms[j + 1] <= i * 5:
                       
                cache[i][j] += cache[i - (denoms[j + 1] // 5)][j]
                
    return cache[-1][-1]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")