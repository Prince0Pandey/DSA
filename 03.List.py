# lst = ["milk", "cheese", "butter", "rice"]
# print("milk" in lst)        # in operator   prints True
# print("bread" in lst)       # in operator   prints False

# for i in range(len(lst)):
#     lst[i] += "+"
#     print(lst[i])


"""Insertion in list"""

# mylst = [1, 2, 3, 4, 5, 6, 7, 8]
# mylst[3] = 12
# mylst[5] = 9
# print(mylst)

# Time Complexity:  O(1)        # Time taken to insert an element is same therefore O(1)
# Space Complexity: O(1)        # insertion does not require any space as memory is already reserved.


""" Insert/Update using insert(), append(), extend() """

# 1. Inserting an element to the beginning of the list

# mylst = [1, 2, 3, 4, 5, 6, 7, 8]
# mylst[0] = "Tree"
# print(mylst)

# Time Complexity:  O(1)
# Space Complexity: O(1)


# 2. Inserting an element to any given place of the list

# mylst = [1, 2, 3, 4, 5, 6, 7, 8]
# mylst.insert(6, "House")
# print(mylst)

# Time Complexity:  O(n)
# Space Complexity: O(1)


# 3. Inserting an element to the end of the list

# mylst = [1, 2, 3, 4, 5, 6, 7, 8]
# mylst.append("DSA")
# print(mylst)

# Time Complexity:  O(1)
# Space Complexity: O(1)


# 4. Inserting another list to the list using extend()

# mylst = [1, 2, 3, 4, 5, 6, 7, 8]
# mynewlst = [9,10,11,12]
# mylst.extend(mynewlst)
# print(mylst)

# Time Complexity:  O(N) Here N is number of element in "mynewlst"
# Space Complexity: O(N) Here N is number of element in "mynewlst"


'''Searching for an element in the list'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 500

# 1. in operator
if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")
# Time Complexity: O(N)


# 2. Linear Search
def linear_search(p_list:list, p_target:int):
    for i, value in enumerate(p_list):          # O(N)
        if value == p_target:                   # O(1)
            return i                            # O(1)
    return -1                                   # O(1)
print(linear_search(my_list, target))

# Time Complexity: O(n)


