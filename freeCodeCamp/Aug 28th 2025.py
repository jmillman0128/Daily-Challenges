##########################################
# freeCodeCamp 8/28/2025 daily challenge
# Solution by Joshua Millman
# Given an array of laptop prices and a budget, return either
# 0 if no laptops are in range
# The most expensive laptop you can afford
# The second most expensive laptop if its in budget
##########################################
def get_laptop_cost(laptops, budget):
    laptopSet = sorted(set(laptops))
    i = 0
    while i <= len(laptopSet) - 1 and budget > laptopSet[i]:
        i += 1
    if i == 0:
        return 0
    elif i == len(laptopSet):
        return laptopSet[-2]
    else:
        return laptopSet[i - 1]
test = get_laptop_cost([2099, 1599, 1899, 1499], 1450)
print(test)