# --- Bubble Sort Algorithm (Reference: https://youtu.be/Vca808JTbI8) ---

# defined function for the Bubble Sort algorithm
def bubble_sort (nums):
    
    for i in range (len(nums)-1, 0, -1): # outer loop
        for j in range (i): # inner loop
            if nums[j] > nums [j+1]: # to determine whether there's a need to swap the values or not
                nums[j], nums[j+1] = nums[j+1], nums[j] #another way of swapping the variables without taking a temp variable
                print (f"Since {nums[j+1]} is greater than {nums[j]}, swap") # to check which values are swapped during each iteration

        print (f"Iteration {j}:", nums) # prints out the entire array after every swapping iteration 

# assigned values to be sorted using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]

# prints out the unsorted array only 
print ("Unsorted list:", assigned_array) 
bubble_sort (assigned_array)

#prints out the final sorted array after going through the swapping iterations
print ("Sorted list using Bubble Sort:", assigned_array)