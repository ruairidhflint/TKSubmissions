# Try writing a Python function to perform a linear search on a set of data.


import math


def linear_search(arr, x):
    answer = 'No matches'
    for index, item in enumerate(arr):
        if item == x:
            answer = f"{x} is found in the array at Index {index}"
            break
        else:
            continue

    return answer


# Try writing a Python function to perform a binary search on a set of data.


def binary_search(sortedArr, x):
    high = len(sortedArr) - 1
    low = 0
    middle = (len(sortedArr) - 1) // 2

    while sortedArr[middle] != x:
        if sortedArr[middle] == x:
            print(high)
            print(low)
            print(middle)
            return sortedArr[middle]

        elif sortedArr[middle] > x:
            high = middle
            middle = middle // 2

        elif sortedArr[middle] < x:
            high = len()
            middle = middle // 2
            print(high)
            print(low)
            print(middle)
            return "Middle value is smaller"

    return sortedArr[middle] - 1


test_arr = [1, 2, 3, 4, 5, 6, 7]
test_arr2 = [1, 2, 3, 4, 5, 6, 7, 8]


print(binary_search([1, 2, 3, 4, 5, 6, 7], 3))


'''

What will the contents of the array below look like after each pass of the Selection Sort algorithm? 

[25, 67, 4, 33, 19, 40]
[4, 67, 25, 33, 19, 40]
[4, 19, 25, 33, 67, 40]
[4, 19, 25, 33, 67, 40]
[4, 19, 25, 33, 67, 40]

What will the contents of the same array look like after each pass of the Insertion Sort algorithm? 
[25, 67, 4, 33, 19, 40]
[4, 25, 67, 33, 19, 40]
[4, 25, 33, 67, 19, 40]
[4, 19, 25, 33, 67, 40]
[4, 19, 25, 33, 40, 67]

'''
