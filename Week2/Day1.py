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
    progress_arr = sortedArr
    current_index = (len(progress_arr) - 1) // 2

    while(progress_arr[current_index] != x):
        if progress_arr[current_index] == x:
            return current_index  # works

        elif progress_arr[current_index] > x:
            progress_arr = sortedArr[:current_index]
            current_index = math.ceil(current_index/2)
        else:
            progress_arr = sortedArr[current_index:]
            current_index = math.ceil(current_index/2)

    return progress_arr[current_index] - 1


'''

'''
test_arr = [1, 2, 3, 4, 5, 6,
            7]  # I want index 3 - length is 7. So 7/3 = 3.5 (round down) or length - 1 / 2
# If I do length - 1 /2 it equals 3.5 so round down
test_arr2 = [1, 2, 3, 4, 5, 6, 7, 8]


print(binary_search([1, 2, 3, 4, 5, 6, 7], 6))


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
