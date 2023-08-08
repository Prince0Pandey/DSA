def Binary_Search(lst, target):
    first_index = 0
    last_index = len(lst) - 1

    while first_index <= last_index:
        midpoint = (first_index + last_index)//2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first_index = midpoint + 1
        else:
            last_index = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = Binary_Search(numbers, 13)
verify(result)

result = Binary_Search(numbers, 3)
verify(result)