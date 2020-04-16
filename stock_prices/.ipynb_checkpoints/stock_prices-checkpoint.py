#!/usr/bin/python

import argparse

def find_max_profit(prices):
    
    high = 0
    h = 0
    
    for i in range(1, len(prices)):
        
        if prices[i] > high:
            
            high = prices[i]
            h = i
    
    return high - min(prices[:h])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))