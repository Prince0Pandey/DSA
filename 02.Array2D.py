import numpy as np
"""
2D Array: Temperature of 4 days at different time interval
Day 1: 11, 15, 10, 6
Day 2: 10, 14, 11, 5
Day 3: 12, 17, 12, 8
Day 4: 15, 18, 14, 9
"""
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)
# Time Complexity:  O(MN)
# Space Complexity: O(MN)


"""insertion of element using insert method in row"""
# newTwoDArray = np.insert(twoDArray,0,[[1,2,3,4]], axis=0)  # 0:index at which we insert, Array, axis = 0:row, 1:column
# print(newTwoDArray)


"""insertion of element using insert method in column"""
# newTwoDArray = np.insert(twoDArray,0,[[101,102,103,104]], axis=1)
# print(newTwoDArray)


"""insertion of element using append method in row"""
"""If we want to append in a row same number of column should present in array which is going to be added"""
# newTwoDArray = np.append(twoDArray, [[101,102,103,104]], axis=0)
# print(newTwoDArray)


"""insertion of element using append method in column"""
"""If we want to append in a column same number of row should present in array which is going to be added
   here the added array have dimension of 1x4 i.e 1 row and 4 column and 'twoDArray' have dimension of 4x4"""
# newTwoDArray = np.append(twoDArray, [[101,102,103,104]], axis=1)
# print(newTwoDArray)

"""
Above code will give an error because the dimensions of the arrays that you're trying to append do not match.

To append to a 2D array along axis=1 (which means appending columns), the new array must have the same number of rows
as the original 2D array.

'twoDArray' have 'n' rows and 'n' column. 
The array you're trying to append ([[101,102,103,104]]) only has one row. i.e 1x4

If you want to append this new array as a column to your existing 2D array, you need to reshape it to have 'n' rows and
1 column.
Here's how you can do it:
"""
# The new array to append
new_array = np.array([1, 2, 3, 4])

# Reshape new_array to have the same number of rows as twoDArray and 1 column
new_array = new_array.reshape(twoDArray.shape[0], -1)

# Append twoDArray to newTwoDArray
newTwoDArray = np.append(twoDArray, new_array, axis=1)
print(newTwoDArray)


"""Accessing element of 2D Array"""


def accessElement(array, rowIndex, columnIndex):
    print(len(newTwoDArray), len(newTwoDArray[0]))
    if rowIndex >= len(newTwoDArray) or columnIndex >= len(newTwoDArray[0]):
        return "Index range out of bound"
    else:
        return array[rowIndex][columnIndex]
print(accessElement(newTwoDArray, 3, 4))
# Time Complexity:  O(1)
# Space Complexity: O(1)


"""Traversing 2D Array"""


def arrayTraversal(array):
    if len(array) > 0:
        for i in range(len(array)):
            for j in range(len(array[0])):
                print(array[i][j], end=" ")
        print()
    else:
        print("array is empty")
arrayTraversal(newTwoDArray)
# Time Complexity:  O(N^2)
# Space Complexity: O(1)


"""Searching for the element in 2d Array"""


def search2DArray(array, value):
    for i in range(len(array)):             # O(mn)
        for j in range(len(array[0])):      # O(n)
            if array[i][j] == value:        # O(1)
                return f"The value is located at Index: {i},{j}"
    return "Value is not in given Array"
print(search2DArray(newTwoDArray, 4))
# Time Complexity:  O(MN)
# Space Complexity: O(1)

"""
Deletion in 2D Array
When we want to delete a row or column in 2D Array we create new array excluding that row or column
"""

new2DArray = np.delete(newTwoDArray, 4, axis=1)     # 4 is the index of the column you want to delete.
print(new2DArray)
# Time Complexity:  O(MN)
# Space Complexity: O(MN)
