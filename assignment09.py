'''

    Write a binary search function. It should take a sorted sequence and the item it is looking for.
    It should return the index of the item if found. It should return -1 if the item is not found.
 
'''


def binary_search(n, lis1):
    for index, item in enumerate(lis1):
        if item == n:
            return index
    return -1


lis1 = [6, 1, 2, 3, 4, 4, 5]
lis1.sort()
print(binary_search(5, lis1))
