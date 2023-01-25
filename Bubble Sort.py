# --- Bubble Sort Algorithm (Reference: https://youtu.be/Vca808JTbI8) ---

# defined function for the Bubble Sort algorithm
def bubble_sort (nums):
    
    for i in range (len(nums)-1, 0, -1):
        for j in range (i): 
            if nums[j] > nums [j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] #another way of swapping the variables without taking a temp variable

# assigned values to be sorted using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]
print ("Unsorted list: ", assigned_array) # prints out the unsorted array only 