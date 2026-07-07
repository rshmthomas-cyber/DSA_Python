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

#len(array) is used to find the length of an array. It returns the number of elements in the array. For example, len([3, 5, 2, 8, 1]) would return 5, since there are 5 elements in the array.
#every element is compared with current largest element.
#Follows O[n] time complexity, where n is the number of elements in the array.
#O(1)space complexity as we are using only a single variable to store the largest element.