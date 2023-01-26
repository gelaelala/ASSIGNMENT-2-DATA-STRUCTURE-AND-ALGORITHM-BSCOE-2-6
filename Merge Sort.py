# --- Merge Sort Algorithm (Reference: https://youtu.be/cVZMah9kEjI) ---

# defined function for the Merge Sort algorithm
def merge_sort (list):
    if len (list) > 1: # in order to split the array in half
        left_list = list[:len(list)//2] # sub array that goes from the beginning of the original array to the middle point
        right_list = list[len(list)//2:] # sub array that goes from the middle point to the end of the original array  

        # for the recursion on both left and right list
        merge_sort (left_list)
        merge_sort (right_list)


# assigned values to be sorted out using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]