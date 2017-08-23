import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import pandas as pd 


'''
    author: Sitansh Rajput
    assumptions:
        * data will be given in a .csv format similar to one presented in .png
        * we must find the list of companies that results in the highest sale
        * price/item does not matter, just end profit
'''


def main():

    # amount of inventory seller has 
    stock = 23

    input = pd.read_csv('input.csv', index_col='Company')
    print(input)

    lists = subset_sum(input['Amount'], stock)
    for list in lists:
        print(list)


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

main()