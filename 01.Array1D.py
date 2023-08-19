"""
NOTE: when we create empty array using numpy module or array module, No memory allocated to the array as there is no
element, The only thing is going to created is 'np_array' object storing metadata of array.

Empty array using array module --> my_array = arr.array('i')
time and space complexity of empty array: O(1)

non-Empty array using array module --> my_array1 = arr.array('i',[1,2,3,4,5,6,7,8])
time and space complexity of non-empty array with N element: O(N)
time taken to copy element to newly created array depends on N i.e number of element
"""

import array as nw

my_array = nw.array('i',[1,2,3,4,5])
print("Before Insertion : ",my_array)

my_array.insert(0,0)
print("After Insertion : ",my_array)

my_array.insert(-9,-1)          # If array index is -ve and out of bound then the element is inserted at first position
my_array.insert(99,6)           # If array index is +ve and out of bound then the element is inserted at last position
print(my_array)

# Time complexity of inserting an element: O(N)
# Space complexity of inserting an element: O(1)

"""
NOTE:If we insert element at the index that is not in range of array index and +ve then it will add the element at the end
of the array
NOTE:If we insert element at the index that is not in range of array index and -ve then it will add the element at the start
of the array
Ex : my_array = nw.array('i',[1,2,3,4,5])
     my_array.insert(109,6)
     my_array.insert(-90,7)
"""

# Array Traversal : to access each element stored in the array so that the data can be checked or used as part of a process.

def array_traversal(array):
    for i in array:
        print(i, end=" ")
    print()
array_traversal(my_array)
# Time complexity of array_traversal(array): O(N)
# Space complexity of array_traversal(array): O(1)      As no space is taken in function

def accessElement(array,index):
    if index >= len(array):
        print("array index out of range")
    else:
        print(array[index])
accessElement(my_array,90)
# Time complexity of accessElement(): O(1)
# Space complexity of accessElement(): O(1)

def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
        return -1
print(linear_search(my_array,64))
# Time complexity of linear_search(): O(N)
# Space complexity of linear_search(): O(1)

"""Deleting an Element from array using remove"""
my_array.remove(-1)
# Time complexity:  O(N)
# Space complexity: O(1)

# 1. Create an array and traverse.
print("Step 01")
my_array1 = nw.array("i",[12,23,34,45,56,67,78,89,90])
for i in my_array1:
    print(i,end=" ")
print()

# 2. Append any value to the array using append() method
print("Step 02")
my_array1.append(100)
print(my_array1)

# 3. Insert value in an array using insert() method
print("Step 03")
my_array1.insert(0,110)
print(my_array1)

# 4. Extend python array using extend() method
print("Step 04")
my_array2 = nw.array('i',[120,130,140,150])
my_array1.extend(my_array2)
print(my_array1)

# 5. Add items from list into array using fromlist() method
print("Step 05")
lst = [160,170,180]
my_array1.fromlist(lst)
print(my_array1)

# 6. Remove any array element using remove() method
print("Step 06")
my_array1.remove(110)       # remove() function only remove first occurrence of element
print(my_array1)

# 7. Remove last array element using pop() method
print("Step 07")
my_array1.pop()
print(my_array1)

# 8. Fetch any element through its index using index() method
print("Step 08")
print(my_array1.index(120))         # Gives index of element 120

# 9. Reverse a python array using reverse() method
print("Step 09")
my_array1.reverse()
print(my_array1)

# 10. Get array buffer information through buffer_info() method
print("Step 10")
print(my_array1.buffer_info())

# 11. Check for number of occurrences of an element using count() method
print("Step 11")
print(my_array1.count(130))

# 13. Convert array to a python list with same elements using list() method
print("Step 13")
lst = list(my_array1)
print(lst)

# 15. Slice Elements from an array
print("Step 15")
new0 = my_array1[0:5:2]
print(new0)

new = my_array1[3:9]
print(new)

new1 = my_array1[:7]
print(new1)

new2 = my_array1[7:]
print(new2)


#Numpy module provides feature rich and high performance array object
"""
Empty array using Numpy module --> np_array = np.array([], dtype=int)
print(np_array)
Non-Empty array using Numpy module --> np_array1 = np.array([4,5,6,7,8], dtype=int)
print(np_array1)
"""