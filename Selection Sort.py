# defined function for the Selection Sort algorithm
def selection_sort (nums):
    for i in range (9):
        min_position = i # this will hold the min position in the array
        for j in range (i, 10):
            if nums [j] < nums [min_position]:
                min_position = j # this will change the min position once the loop finds a value lower than the current min position

        # for swapping the values inside the array

# assigned array values to be sorted using the algorithm
nums = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]