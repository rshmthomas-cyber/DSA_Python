"""
Problem : Check if an array is sorted in ascending order.

Approach:
- Traverse the array from array import array

from the first element to the second last element.
- Compare each element with the next element.
- If any element is greater than the next element, the array is not sorted.
- If the loop completes without finding any such pair, the array is sorted

Time Complexity: O(n)
Space Complexity: O(1)

Author: Reshma Thomas
"""

def is_sorted(arr):
    if len(arr) < 2:
        return True  # An array with 0 or 1 element is considered sorted
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True     
answer = is_sorted([1,2,3,4,5])
print(answer)