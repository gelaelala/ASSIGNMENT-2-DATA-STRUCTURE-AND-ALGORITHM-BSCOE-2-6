# --- Insertion Sort Algorithm (Reference: https://youtu.be/lEA31vHiry4) ---

# defined function for the Insertion Sort algorithm
def insertion_sort (list):
    for index in range (1, len(list)):
        value = list[index]
        i = index - 1 # in order to compare the value to the left of it
        while i >= 0: # to further compare the value by pushing i further and further to the left
            if value < list [i]: # if the statement is true, it will shift list[i] to the right
                list [i+1] = list[i] # shift the number in slot i right to slot i+1
                list[i] = value # shift value left into slot i

                print (f"\nSwap {list[i+1]} with {list[i]}")

                i = i - 1 # to decrement i in order to compare value to something lower
            else: 
                break # if the value is not less than the item being compared to, meaning the value is in the right place already

            print (list) # prints out array after every swapping of element

# assigned values to be sorted out using the algorithm
assigned_array = [79, 33, 95, 54, 97, 11, 90, 89, 64, 19]

# prints out the unsorted array only
print ("Unsorted list:", assigned_array)
insertion_sort (assigned_array)

# prints out the sorted array
print ("\nSorted list using Insertion Sort:", assigned_array)