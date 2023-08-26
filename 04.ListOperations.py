# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# myList[:2] = ['x', 'y']           #assigning 2 values at a time
# print(myList[:])

"""
List methods for deletion
1. pop(): this will delete the last element from the list and return it, if no arguments/index is passed.
2. delete(): will delete the specified index value or specified slice. SYNTAX: del myList[:2]
3. remove(): will delete the element given as argument example: "a", 2, etc
"""

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# myList.pop()                                  # O(1)
# print(myList)

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# myList.pop(1)                                 # O(N)
# print(myList)

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# print(myList.pop())     # prints element that is being deleted
# print(myList)

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# del myList[1]                                 # O(N)
# print(myList)

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# del myList[:2]
# print(myList)

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# print(myList[::2])                         # will print ['a', 'c', 'e']
# del myList[::2]                            # will delete ['a', 'c', 'e']
# print(myList)                              # will print ['b', 'd', 'f']

# myList = ['a', 'b', 'c', 'd', 'e', 'f']
# myList.remove("e")                           # O(N)
# print(myList)


"""List Operations / Function"""

# + Operator: Concatenate Lists
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)


# * Operator: repeat the list element Lists
# a = [1, 0]
# a *= 2
# print(a)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1.max(): returns the item with the highest value in the list
print(f"Maximum: {max(a)}")

# 2.min(): returns the item with the lowest value in the list
print(f"Minimum: {min(a)}")

# 3.sum(): returns the sum of all the items in the list
print(f"Sum: {sum(a)}")

print(f"Average: {sum(a) / len(a)}")

"""Strings and List"""
a = "spam"
b = list(a)
print(b)

x = "spam spam spam"
y = x.split()  # if not specified then by default takes space as a seperator
print(y)

m = "spam-spam-spam"
n = m.split("-")
print(n)

delimiter = "a"
o = m.split(delimiter)
print(o)

# o = ['sp', 'm-sp', 'm-sp', 'm']
print(delimiter.join(o))  # join will joint the list into one string


'''Average of numbers given by user'''
# total = 0
# count = 0
# while True:
#     inp = input("Enter number to perform average: ")
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total/count
# print("Average:", average)


'''Problem: Average of numbers given by user using List & List Functions'''
# mylist = list()
# while True:
#     inp = input("Enter number to perform average: ")
#     if inp == 'done': break
#     value = float(inp)
#     mylist.append(value)
# average = sum(mylist) / len(mylist)
# print("Average:", average)


"""MY Way"""
# inp = input("Enter numbers separated by space: ")
# lst = inp.split()
# lst = [int(item) for item in lst]
# print("Average:", sum(lst) / len(lst))

"""Pitfalls and ways to avoid them"""

myList = [4, 6, 1, 7, 3, 0, 8, 2, 5, 9]

# 1.sort() does not return any value, therefore it will print 'None'
# print(myList.sort())

# myList.append(10)                       # will append 10
# print(myList)

# myList.append([10])                     # will append [10]
# print(myList)

# myList = myList + [10]                  # will append 10
# print(myList)

# 2. Store the original list using temporary variable
# temp = myList[:]
# temp.sort()
# print(f"original list: {myList}")
# print(f"Sorted list: {temp}")

# 3. if we don't want to change the original list we can use sorted()
# print(f"Temporary sorted list: {sorted(myList)}")
# print(f"original list: {myList}")


"""Arrays vs Lists"""
import numpy as np

# 1. Arithmetic Operations: can be done on array not on list
# myarray = np.array([1, 2, 3, 4, 5, 6])
# newList = [1, 2, 3, 4, 5]
# print(myarray/2)                    # will divide all values by 2
#
# print(newList/2)                    # will throw error

# 2. Data Types: Array doesn't support multiple data types at a time but list does
# myarr = np.array([3, 4, 6, 1, 'a'])           # myarr will be changed to string from int
# newlst = [9, 5, 6, 'a']
# print(myarr)
# print(newlst)


"""List Comprehension"""
# SYNTAX: new_list = [new_item for item in list]

# lst = [1, 2, 3]
# lst1 = []
# for i in lst:
#     multiply_2 = i*2
#     lst1.append(multiply_2)
# print("Given List:", lst)
# print("Derived List:", lst1)

# Above code can be written as given below
# lst = [1, 2, 3]
# lst1 = [i*2 for i in lst]
# print("Given List", lst)
# print("Derived List using List Comprehension:", lst1)

# language = "Python"
# lst = [letter for letter in language]
# print(lst)


"""Conditional List Comprehension"""
# SYNTAX: new_list = [new_item for item in list if Condition]

# given_list = [-1, 10, -20, 2, -90, 60, 45, 15]
# new_list = [number for number in given_list if number > 0]
# print(new_list)

# given_list = [-1, 10, -20, 2, -90, 60, 45, 15]
# new_list = [number*number for number in given_list if number < 0]   # List of Square of negative number
# print(new_list)

sentence = 'My name is Prince'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels        # returns True or False

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


"""Conditional List Comprehension"""
# SYNTAX: new_list = [new_item if else Condition for item in list]

given_list = [-1, 10, -20, 2, -90, 60, 45, 15]
new_list = [number if number > 0 else "Negative Number" for number in given_list]
print(new_list)


def get_number(number):
    return number if number > 0 else "Negative Number"

given_list = [-1, 10, -20, 2, -90, 60, 45, 15]
new_list = [get_number(number) for number in given_list]    # Same as above but function is used instead of condition
print(new_list)