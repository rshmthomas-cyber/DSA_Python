"""
Problem: Second Largest Element

Time Complexity: O(n)
Space Complexity: O(1)

Concept Learned:
Maintain two states:
1. largest
2. second_largest
"""


def second_largest(arr):
    if len(arr) <2:
        return None  # Return None if there are less than 2 elements
    largest = arr[0]
    second_largest = None
    for number in arr[1:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number != largest:
            if second_largest is None or number > second_largest:
                second_largest = number
    return second_largest
answer = second_largest([3, 5, 2, 8, 1])
print(answer)