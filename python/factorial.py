# DESCRIPTION AND STRATEGY
# Factorial(5) is written as 5! and is defined as 5! =  5 * 4 * 3 * 2 * 1. 
# Similarly, Factorial(3) is 3! and is defined as 3! = 3 * 2 * 1
# We will use recursion, dividing our approach into two parts: the base case and recursive case. 
# The base case would be when we reach 1, and the recursive case will be: x * Factorial(x - 1)

# BIG O NOTATION
# Logarithmic: O(log n)

# CODE
# factorial takes an integer, and returns the product of it and all natural numbers that precede it that are > 0;

def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x - 1)

