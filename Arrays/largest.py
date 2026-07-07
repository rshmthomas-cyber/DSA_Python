"""
Problem: Largest Element in an Array

Approach:
- Maintain the largest element seen so far.
- Traverse the array once.
- Update the largest value whenever a bigger element is found.

Time Complexity: O(n)
Space Complexity: O(1)

Author: Reshma Thomas
"""
def find_largest(arr):
    if len(arr) == 0:
        return None  # Return None for empty array
    largest = arr[0]
    for number in arr:
        if number > largest:
            largest = number
    return largest
answer = find_largest([3, 5, 2, 8, 1])
print(answer)

