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