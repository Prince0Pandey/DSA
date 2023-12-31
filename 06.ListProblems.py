import numpy as np
"""Q1. Two Sum/Find Pairs: Program to find all pairs of integer whose sum is equal to given number
ex. lst = [1,2,3,4,5,6] target = 6 --> [2,4] note that [3,3] not allow i.e same number"""
print("Problem 01")


def findPairs(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print([i, j])
mylst = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(mylst, 6)


"""Q2. Finding a number in an array"""
print("\nProblem 02: Find Number in Array")
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def findNumber(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            return i
    return -1
print(findNumber(myArray, 21))


"""Q3. Max Product of two numbers"""
"""My way"""
print("\nProblem 03: Max Product of 2 number in Array")


def max_product(arr):
    max1 = 0
    max2 = 0
    for number in arr:
        if number > max1:
            max1 = number
    for number in arr:
        if max2 < number < max1:
            max2 = number
    return max1*max2
print(max_product([1, 7, 3, 4, 9, 5]))


"""Q4. Missing Number in an array"""
print("\nProblem 04: Missing Number Array")


def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) / 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    return missing
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5


"""Q5.Given 2D list calculate the sum of diagonal elements."""
print("\nProblem 05: Array Diagonal Sum")


def diagonal_sum(mat):
    sumOfDiagonal = 0
    for i in range(len(mat)):
        sumOfDiagonal += mat[i][i]
    return sumOfDiagonal
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # 15


"""
Q6. Write a function to remove the duplicate numbers on given integer array/list.
Example
remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""
print("\nProblem 06: Remove Duplicate")


def remove_duplicates(arr):
    arr = list(set(arr))
    return arr
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


print("\nProblem 06 2nd Way: Remove Duplicate")


def delete_duplicate(arr):
    arr1 = []
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    return arr1
print(delete_duplicate([1, 1, 2, 2, 3, 4, 5]))


print("\nProblem 06 3rd Way: Remove Duplicate")


def rm_duplicate(arr):
    new = []
    [new.append(item) for item in arr if item not in new]
    return new
print(rm_duplicate([1, 1, 2, 2, 3, 4, 5]))


"""
Q7. Write a function to find all pairs of an integer array whose sum is equal to a given number.
Do not consider commutative pairs.
Example:
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']

Note:
4+3 comes from second and third index elements from the main list.
3+4 comes from third and seventh index elements from the main list.
"""
print("\nProblem 07: Pair_sum")


def pair_sum(myList, sumOfPairs):
    lst = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sumOfPairs:
                lst.append(f"{myList[i]}+{myList[j]}")
    return lst
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))


"""
Q8. Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
Example :
Input: nums = [1,2,3,1]
Output: true
"""
print("\nProblem 08: Contains Duplicate")


def contains_duplicate(nums):
    tup = list(set(nums))
    return False if nums == tup else True
print(contains_duplicate([1, 2, 3, 1]))


"""
Q9. You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Example:
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
                 
Output:matrix = [[7, 4, 1],
                 [8, 5, 2],
                 [9, 6, 3]]
"""
print("\nProblem 09: Rotate Matrix By 90 Degree")


def rotate(mat1):
    n = len(mat1)

    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]

    # Reverse each row
    for row in mat1:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
    return mat1

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(rotate(matrix))
