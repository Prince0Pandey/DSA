mytuple1 = (1, 4, 2, 6)
mytuple2 = (4, 0, 7, 0, 8, 9, 0, 1)
print("Concatenation using + operator:", mytuple1 + mytuple2, "\n")
print("* used for that many times:", mytuple1 * 3, "\n")
# NOTE : we cannot multiply 2 tuple using '*' operator
print("Searching element using 'in' Operator:", 4 in mytuple1, "\n")

# returns count of the element in tuple
print("Element Frequency in tuple using count():", mytuple2.count(0), "\n")

# returns the index the element
print("Returns index of given element/argument:", mytuple2.index(0), "\n")

print("Returns No. Of element in tuple:", len(mytuple2), "\n")

print("Returns Max of tuple using max():", max(mytuple2), "\n")

print("Returns Min of tuple using min():", min(mytuple2), "\n")

print("List to tuple using tuple() method:", tuple([1, 2, 3, 4, 5]))

