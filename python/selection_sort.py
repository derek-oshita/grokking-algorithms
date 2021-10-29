# DESCRIPTION AND STRATEGY
# Take a list of artists you listen to, for example. Each artist has an integer representing how many times you've played that artist.
# To sort by most played, you would need to check every artist O(n), then add the highest played artist to a new list.
# You would take that same list, now one artist shorter, and repeat that process n times until you reach the least played artist.

# BIG O NOTATION
# Quadratic: O(log N)

# Note: it's true that each time you visit the old list, it is smaller than the original n elements. 
# You check n elements first, then n - 1, then n -2, etc...
# On average, you check a list that has .5 of n elements. The actual runtime is O(n x .5 x n)
# After dropping the constant (.5), we are left with O(n * n) or O(n^2). Selection is a slow algorithm!

# CODE

# find_smallest is a helper function that takes an array of integers and returns the index of the smallest int.
def find_smallest(arr): 
    # take the first element as the smallest value
    smallest_value = arr[0]
    # store the index of the smallest value 
    smallest_value_index = 0
    # iterate over the arr, starting at index 1 since we defined the smallest value at index 0
    for i in range(1, len(arr)):
        # if the current value is smaller than our smallest value, reassign the smallest value and its index
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_value_index = i
    return smallest_value_index

# selection_sort will use this helper function to find the index of the smallest value in our original array,
# append that value to a new array, then remove it from our original array.
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # use helper function to get the index of the smallest value
        smallest_value_index = find_smallest(arr)
        # take that index to get the value, append it to new_arr, then remove it from arr
        new_arr.append(arr.pop(smallest_value_index))
    return new_arr

some_arr = [7, 1, 3, 2, 5, 4, 0, 6]

print(selection_sort(some_arr))
# => [0, 1, 2, 3, 4, 5, 6, 7]

        