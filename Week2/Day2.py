'''Write a recursive search function that receives as input an array of integers and a target integer value. This function should return True if the target element exists in the array, and False otherwise.
'''

def recursive_search(arr, target):
    if len(arr) == 0:
        return False
    
    if arr[0] == target:
        return True
    else:
        return recursive_search(arr[1:], target)


print(recursive_search([1,2,3,4,5,6,7,8], 5))

def recursive_search_two(arr,target,position=0):
    if position == len(arr) - 1:
        return False

    if arr[position] == target:
        return True
    else: 
        return recursive_search_two(arr, target, position + 1)

print(recursive_search_two([1,2,3,4,5,6,7,8], 50))

'''What would be the base case(s) we’d have to consider for implementing this function?

- For first implementation: If the list has length or if the list target and the list position match
- For second implementation: if the position is equal to the length of the list
'''