#To find largest element in an array
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
