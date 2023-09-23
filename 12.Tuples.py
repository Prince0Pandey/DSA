# Empty tuple using tuple()
empty = tuple()
print("Empty tuple:", empty)

# Creating tuple with 1 element requires comma at the end
one_tuple = ("Fruits",)
print("Tuple with one element:", one_tuple)

# Creating tuple using Parenthesis
my_tuple = (1, 2, "three", 4, True)
print("Tuple with Parenthesis:", my_tuple)

# Creating tuple without Parenthesis
myTuple = 1, 2, "three", 4, True
print("Tuple without Parenthesis:", myTuple)
# NOTE: tuple() takes only one argument i.e in string format & separate each element

# Creating tuple with elements using tuple()
Tuple1 = tuple("12345asd")
print("tuple with elements using tuple():", Tuple1)

"""
Time Complexity: O(1)
Space Complexity: O(N)
"""

# ACCESS TUPLE ELEMENT
print("\nACCESS TUPLE ELEMENT")
newTuple = tuple("abcde")
print("Element at 2nd Index:", newTuple[2])
print("Element at 2nd Last Index:", newTuple[-2])
print("Element using Slice[] Operator", newTuple[1:4], "\n")

# TRAVERSE TUPLE ELEMENT
print("\nTRAVERSE TUPLE ELEMENT")
for element in newTuple:
    print(element, end=" ")

print("\n\nTRAVERSE TUPLE ELEMENT")
for i in range(len(newTuple)):
    print(newTuple[i], end=" ")

# SEARCH FOR ELEMENT IN TUPLE
print("\n\nSEARCH ELEMENT")
print("using 'in' Operator:", "a" in newTuple)          # Time Complexity: O(N)
print("using 'in' Operator:", "ab" in newTuple)

print("\nUsing index():", newTuple.index("d"))          # Time Complexity: O(N)

print("\nSearch element using function:")
def searchTuple(tpl, element):
    for i in range(len(newTuple)):
        if tpl[i] == element:
            return f"The {element} is found at {i} index"
    return "The element is not found"

print(searchTuple(newTuple, "b"))
print(searchTuple(newTuple, "ab"))


