myDict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    0: "zero"
}
print(0 in myDict)                  # will print True as it is present in dict

print("one" in myDict)              # will print false, although it is present which implies that 'in' function
                                    # does not work on values

print("three" in myDict.values())   # print True

print("six" in myDict.keys())       # print False

print("six" not in myDict.keys())   # print True

print(len(myDict))                  # print 6


myDict1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
}       # All True

myDict2 = {
    0: "zero",
    False: "False"
}       # All False

myDict3 = {
    1: "One",
    False: "False"
}       # 1 True & 1 False

myDict4 = {
    0: "Zero",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
}       # 1 False

"""
all() returns True if all keys are True Else False

True  -> if all keys are True (True means (string, number) except zero)
False -> if all keys are False (False means 0 or 'False')
False -> if one key is True
False -> if one value is False
"""
print(all(myDict1))           # returns True
print(all(myDict2))           # returns False
print(all(myDict3))           # returns False
print(all(myDict4), "\n")     # returns False


"""
any() returns False if all key are False Else True

False  -> if all keys are False
True -> if all keys are True
True -> if one key is True
True -> if one value is False
"""
print(any(myDict1))           # True
print(any(myDict2))           # False
print(any(myDict3))           # True
print(any(myDict4), "\n")     # True

print(sorted(myDict))   # returns sorted list of keys
