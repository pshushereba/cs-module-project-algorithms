'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# U - Understand
# The function receives a list of numbers.
# Should return a single number
# The list will contain pairs of numbers; one number will be in the list only once.

# P - Plan
# .count() list method?

# E - Execute

# R - Reflect
# Can maybe do this with list comprehension?
# Should figure out the run time of this.