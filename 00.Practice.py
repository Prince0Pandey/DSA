# Adding 2 list

# numbers = [1,2,3,4,5]
# numbers01 = [6,7,8,9]
# numbers.extend(numbers01)
# print(numbers)

# Array

import array as myarray
arr1 = myarray.array("i",[1,2,3,4,5,67,9])        # creating array
print(arr1)

lst = list(range(1,101))
arr2 = myarray.array("i",lst)

print(lst)
print(arr2)