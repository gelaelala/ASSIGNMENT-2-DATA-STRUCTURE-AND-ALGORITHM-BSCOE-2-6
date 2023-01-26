# --- Merge Sort Algorithm (Reference: https://youtu.be/cVZMah9kEjI) ---

# defined function for the Merge Sort algorithm
def merge_sort (list):
    if len (list) > 1: # in order to split the array in half
        left_list = list[:len(list)//2] # sub array that goes from the beginning of the original array to the middle point
        right_list = list[len(list)//2:] # sub array that goes from the middle point to the end of the original array  

        print ("\nLeft List:", left_list)
        print ("Right List:", right_list)

        # for the recursion on both left and right list
        merge_sort (left_list)
        merge_sort (right_list)

        # implementation of the merge step
        i = 0 # leftmost element of the left array/left_list index
        j = 0 # leftmost element of the right array/right_list index
        k = 0 # index in the merged array

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list [i] # save the value of the left array inside of merged array
                i += 1
            else:
                list[k] = right_list[j] # save the value of the right array inside of merged array
                j += 1
            k += 1 

        # transfer every element from the left array to the merged array without considering the right array
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1 

        # if it's still not at the end of the right array, transfer elements to the merged array    
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1 
            k += 1

        print (list) # prints out every merged array 

# assigned values to be sorted out using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]

# prints out the unsorted array only
print ("Unsorted list:", assigned_array)

merge_sort (assigned_array)

#prints out the sorted array with the use of the algorithm
print ("\nSorted list using Merge Sort:", assigned_array)