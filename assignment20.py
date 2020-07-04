'''
Write a Python class to find the three elements that sum to zero
from a list of n real numbers. 
Input array: [-25, -10, -7, -3, 2, 4, 8, 10] 
Output : [[-10, 2, 8], [-7, -3, 10]]

'''
from itertools import combinations


def sumToZero(inArray):
    comb = combinations(inArray, 3)
    posibOutComes = list(comb)
    res = []
    for i in posibOutComes:
        if sum(i) == 0:
            res.append(list(i))
    return res


inArray = [-25, -10, -7, -3, 2, 4, 8, 10]
print(sumToZero(inArray))
