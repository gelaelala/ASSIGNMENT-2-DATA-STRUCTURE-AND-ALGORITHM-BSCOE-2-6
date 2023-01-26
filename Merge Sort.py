# --- Merge Sort Algorithm (Reference: https://youtu.be/cVZMah9kEjI) ---

# defined function for the Merge Sort algorithm
def merge_sort (list):
    if len (list) > 1: # in order to split the array in half
        left_list = list[:len(list)//2] # sub array that goes from the beginning of the original array to the middle point
        right_list = list[len(list)//2:] # sub array that goes from the middle point to the end of the original array  

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


# assigned values to be sorted out using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]