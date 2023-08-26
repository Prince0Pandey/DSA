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

myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.remove("e")                           # O(N)
print(myList)




