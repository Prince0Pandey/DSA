# Creating empty dictionary using dict()
my_dict = dict()
print(my_dict)

eng_sp = dict(one="uno", two="dos", three="tres")
print(eng_sp)

eng_sp2 = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_sp2)
print(eng_sp == eng_sp2)

eng_sp_list = [("one", "uno"), ("two", "dos"), ("three", "tres")]
eng_sp3 = dict(eng_sp_list)
print("(List of tuple) to dictionary:", eng_sp3)

my_dict1 = {"name": "Prince", "Age": "21"}
print(my_dict1)

my_dict1["Age"] = 23
my_dict1["Address"] = "Mumbai"              # if key is not present then it will add new key-value pair to end
print(my_dict1, "\n")

print("Traversing Dictionary")
def traverseDict(dict):
    for key in dict:
        print(key, ":", dict[key])
traverseDict(my_dict1)
print()


def searchDict(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return f"{key}:{value}"
    return "Value does not exist"

print(searchDict(my_dict1, 23))
print(searchDict(my_dict1, 123), "\n")

# Delete/Remove an element from the Dictionary
person = {"name": "Prince Pandey", "age": 23, "education": "Graduation", "Degree": "B.E",
          "field": "Information Technology"}

del person["Degree"]
print(person)

deleted_element = person.pop("education", None)
# if key error occurs it will print none and doesn't break the code
# pop() will only return value not key
print("Deleted Element (value):", deleted_element, "\n")
print(person, "\n")

remove_element = person.popitem()     # popitem() will pop the last element and returns key:value pair
print("Removed Element(key:value):", remove_element)
print(person, "\n")

person.clear()      # will clear the dictionary / O(N):N means number of key,value pairs in dict
print(person, "\n")

