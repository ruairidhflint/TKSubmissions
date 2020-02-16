# Try writing a Python function to perform a linear search on a set of data.


def linear_search(arr, x):
    answer = 'No matches'
    for index, item in enumerate(arr):
        if item == x:
            answer = f"{x} is found in the array at Index {index}"
        else:
            continue

    return answer


print(linear_search([1, 2, 3, 4, 5, 6], 5))

# Try writing a Python function to perform a binary search on a set of data.

def binary_search(sortedArr, x):
    