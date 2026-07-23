"""
Problem: To remove duplicates from sorted array.

Solution: Use two pointer system

Time complexity: O(n)

Space complexity: O(1)
"""
def remove_duplicates(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i+=1
    return i+1 


#test cases
arr = [1,1,2,3,4,4,5]
length = remove_duplicates(arr)
print(f"Length: {length}")
print(f"Unique: {arr[:length]}")
print(f"Whole array: {arr}")

  # Output: Length: 5, Unique: arr[:length] = [1, 2, 3, 4, 5]
