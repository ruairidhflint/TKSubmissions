'''Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, write a function rotate_image that receives a matrix as input and rotates the image by 90 degrees in the counter-clockwise direction.

Thoughts: 

[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 1, 2, 3],
 [4, 5, 6, 7]]

Rotated 90 degrees counter clockwise

[[4, 9, 5, 1],
 [5, 1, 6, 2],
 [8, 2, 7, 3],
 [7, 3, 8, 4]]

 After a 90 degree rotatation, the first elements in each array become the first array, the second elements
 become the ordered elements in the second array etc etc if it's clockwise...

 for counter clockwise, the last element of each array becomes the elements in the first array, the working backwards etc. 

'''

test_case = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 1, 2, 3],
             [4, 5, 6, 7]]


def rotate_image(matrix):
    # create empty matrix container (list of four empty lists)
    rotated_image = []

    # starting with the first list, append the last element to the rotated first list

    temp_arr = []
    position = len(matrix) - 1

    while len(rotated_image) != len(matrix):
        temp_arr = []
        for x in range(0, len(matrix)):
            temp_arr.append(matrix[x][position])
        rotated_image.append(temp_arr)
        position -= 1

    return rotated_image

'''
Run time analysis...very poor. O(n^2) (nested loops).

'''

print(rotate_image(test_case))