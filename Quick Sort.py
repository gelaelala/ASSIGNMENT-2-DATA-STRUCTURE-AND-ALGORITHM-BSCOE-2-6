# --- Quick Sort Algorithm (Reference: https://youtu.be/9KBwdDEwal8) ---

# defined function for the Quick Sort algorithm
def quick_sort (arr, left, right): # left and right are indexes that determine the part of the array that we want to sort, left = 0 while right = len(arr)  
    if left < right: # to check if subarray contains at least two elements
        partition_pos = partition(arr, left, right) 
        quick_sort(arr, left, partition_pos - 1) # calls all elements less than the pivot element 
        quick_sort(arr, partition_pos + 1, right) # calls all elements that are greater than the pivot element

def partition (arr, left, right): # returns the index of the pivot element 
    i = left # left point of the area to sort
    j = right - 1 # point right of the pivot
    pivot = arr[right] # pivot element itself

    while i < j: # to check if i and j crossed
        while i < right and arr[i] < pivot: # while i is not at the end of the array and the element at index i is less than the pivot element
            i += 1 # will move i to the right 

        while j > left and arr[j] >= pivot:
            j -= 1 # this will move j to the left
        
        if i < j: # to check if i and j have crossed yet

# assigned values to be sorted out using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]