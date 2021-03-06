# Try writing a Python function to perform a linear search on a set of data.


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
    low_value = 0
    high_value = len(sortedArr) - 1

    while low_value <= high_value:
        mid_value = (low_value + high_value) // 2
        if sortedArr[mid_value] > x:
            high_value = mid_value - 1
        elif sortedArr[mid_value] < x:
            low_value = mid_value + 1
        else:
            return mid_value
    return "Does not exist in list"

print(binary_search([1, 2, 3, 4, 5, 6, 7], 99))

# Can you rewrite the above function so that it uses recursion?



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
