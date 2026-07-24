def move_zeroes(arr):
    """
    Problem: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

    Approach:
    - Use two pointers to traverse the array.
    - One pointer (i) will track the position to place the next non-zero element.
    - The other pointer (j) will traverse the array.
    - When a non-zero element is found, it is placed at the position of pointer i, and i is incremented.
    - After traversing the array, fill the remaining positions with zeroes.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return arr
    i = 0
    for j, value in enumerate(arr):
        if value!= 0:
            arr[i] = value
            arr[j] = 0  # Optional: Set the current position to zero after moving the non-zero element  
            i+=1 
    
    return arr
result = move_zeroes([0,1,0,0,3,12])
print(result)

#My invariant: Before index i, we've placed all the non-zero elements we've encountered so far, preserving their original order.
