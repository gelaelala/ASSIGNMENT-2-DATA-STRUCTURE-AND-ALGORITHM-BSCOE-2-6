# --- Selection Sort Algorithm (Reference: https://youtu.be/5KjapFQNxUo) ---

# defined function for the Selection Sort algorithm
def selection_sort (nums):
    for i in range (9):
        min_position = i # this will hold the min position in the array
        for j in range (i, 10):
            if nums [j] < nums [min_position]:
                min_position = j # this will change the min position once the loop finds a value lower than the current min position

        # for swapping the values inside the array
        temp = nums [i]
        nums [i] = nums [min_position]
        nums [min_position] = temp
        print (nums) # this will print how it looks like when swapping elements in every iteration

# assigned array values to be sorted using the algorithm
nums = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]

print ("Unsorted list:", nums) # prints out the unsorted list only
print ("\n")
selection_sort (nums)

print ("\nSorted list using Selection Sort:", nums) # this will print the sorted array only