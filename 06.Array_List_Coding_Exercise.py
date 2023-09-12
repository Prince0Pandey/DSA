"""Q1. Two Sum/Find Pairs: Program to find all pairs of integer whose sum is equal to given number
ex. lst = [1,2,3,4,5,6] target = 6 --> [2,4] note that [3,3] not allow i.e same number"""
print("Problem 01")
def findPairs(nums:list, target:int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print([i, j])
mylst = [1,2,3,2,3,4,5,6]
findPairs(mylst, 6)


"""Q2. Finding a number in an array"""
print("Problem 02")
import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
def findNumber(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            return i
    return -1
print(findNumber(myArray, 21))

"""Q3. Max Product of two element"""
"""My way"""
print("Problem 03")
def max_product(arr):
    max1 = 0
    max2 = 0
    for number in arr:
        if number > max1:
            max1 = number
    for number in arr:
        if number > max2 and number < max1:
            max2 = number
    return max1*max2

print(max_product([1, 7, 3, 4, 9, 5]))

"""2nd Way"""
print("Problem 03 2nd Way")
def max_product(arr):
    max1 = 0
    max2 = 0
    for number in arr:
        if number > max1:
            max1 = number
            max2 = max1
        elif number > max2:
            max2 = number
    return max1*max2

print(max_product([1, 7, 3, 4, 9, 5]))


"""Q4. Missing Number in an array"""
print("Problem 04")
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    return missing
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5

"""Q5.Given 2D list calculate the sum of diagonal elements."""
print("Problem 05")
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

