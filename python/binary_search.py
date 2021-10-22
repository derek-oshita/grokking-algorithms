# STRATEGY
# With binary search, you guess in the middle and eliminate half the remaining options every iteration.
# Binary search only works when the list that is passed is sorted.

# BIG O NOTATION
# Logarithmic: O(log N)

# DESCRIPTION
# binary_search takes a sorted list and the item we are looking for as parameters.
# In this case, we are looking for an integer.

def binary_search(list, item): 
    # sort the list in case it is not sorted
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        # found the item
        if guess == item:
            return mid
        # guess was too high
        if guess > item:
            high = mid - 1
        # guess was too low
        else:
            low =  mid + 1
    # if we exit the while loop, we return none
    return None

# TEST CASES
list_one = [1, 3, 5, 7, 9]
num_one = 3
# => 1
list_two = [9, 921, 5, 102, 23, 99, 4, 1, 13]
num_two = 23
# => 5

# OUTPUT
print(binary_search(list_two, num_two))