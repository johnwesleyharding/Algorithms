#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
    
    def eatonacci(n):    
        n -= 1
        if n > 2:        
            e = eatonacci(n)
        else:
            return [0, 0, 1, 2]
        e.append(e[-1] + e[-2] + e[-3])
        return e
    
    return 1 + sum(eatonacci(n)[:n + 1])

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
        
    else:
        print('Usage: eating_cookies.py [num_cookies]')