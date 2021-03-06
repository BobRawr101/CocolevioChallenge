import pandas as pd


'''
    author: Sitansh Rajput
    assumptions:
        * data will be given in a .csv format similar to one presented in .png
        * we must find the list of companies that results in the highest sale
        * price/item does not matter, just highest sale
'''


def main():

    # amount of inventory seller has 
    stock = 23

    data = pd.read_csv('input.csv', index_col='Company')
    print('Input Data:')
    print(data, '\n')

    lists = subset_sum(data, stock)
    best_combo, best_profit = find_best(data, lists)

    print('Best Combination:')
    print(best_combo, '\n')
    print('Best Profit Achieved:')
    print(best_profit)


def subset_sum(data, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(data.index):
        remaining = data[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + data.loc[n]['Amount'])


def find_best(data, lists):
    best_combo = []
    best_profit = 0  
    
    print('List of Combinations')
    for buyers in lists:
        print(buyers)
        temp_profit = 0
        for buyer in buyers:
            temp_profit += data.loc[buyer]['Price']
        if temp_profit > best_profit:
            best_profit = temp_profit
            best_combo = buyers
    print('\n')
    return best_combo, best_profit


main()