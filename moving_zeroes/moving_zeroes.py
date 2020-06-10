'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[j] > arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# U - Understand:
# The input is a list of integers.
# Need to move non-zero numbers to the left side of the list and return altered list.
# Can an empty list be valid input?
# How to deal with negative numbers?

# P - Plan:
# Can we use selection sort but change the way that we're comparing?
# Built in Python sort() method?
