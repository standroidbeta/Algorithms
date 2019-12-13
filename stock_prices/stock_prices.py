#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) == 1:
        return 0
    lowest_price = prices[0]
    profit = prices[1] - prices[0]

    for price in prices[1:]:
        if (price - lowest_price) > profit:
            profit = price - lowest_price
        if price < lowest_price:
            lowest_price = price

    print(f"A profit of ${profit} can be made from the current stock price of ${lowest_price}.")

    return profit


stock1 = [10, 7, 5, 8, 11, 9]
stock2 = [100, 90, 80, 50, 20, 10]
stock3 = [1050, 270, 1540, 3800, 2]
stock4 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]

find_max_profit(stock1)
find_max_profit(stock2)
find_max_profit(stock3)
find_max_profit(stock4)

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
