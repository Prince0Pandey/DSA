"""Dictionary Methods"""
person1 = {"name": "Prince Pandey", "age": 23, "education": "Graduation", "degree": "B.E",
           "branch": "Information Technology"}

"""
copy(): will copy the dictionary to new dict
dictionary.copy()
"""
print("Copy Method")
person2 = person1.copy()
print(person1)
print(person2, "\n")


"""
fromkeys()
dictionary.fromkeys(sequence[], values): creates a dictionary from given argument
"""
print("FromKeys Method")
newDict = {}
newDict = newDict.fromkeys([1, 2, 3, 4, 5], 10)     # value is ten for all keys
print(newDict)

newDict1 = {}.fromkeys([1, 2, 3, 4, 5], 0)          # value is zero for all keys
print(newDict1)

newDict2 = {}.fromkeys([1, 2, 3, 4, 5])          # value will be 'None' for all keys
print(newDict2, "\n")


"""
get()
dictionary.get(key, value): value parameter is optional
when key does not present in dict then value will be printed(value is optional Parameter)
"""
print("Get Method")
print(person1.get("branch", "key does not exist"))  # if key present in dict then return its value
print(person1.get("city", "key does not exist"))
print(person1.get("city"),  "\n")    # returns None as 'Value' parameter is not provided & key 'city' is not present


"""
items()
dictionary.items() -> returns dictionary key:value as tuple(key, value) inside list
"""
print("Item Method")
print(person1.items(), "\n")


"""
keys()
dictionary.keys() -> returns list of keys
"""
print("Keys Method")
print(person1.keys(), "\n")


"""
values()
dictionary.values() -> returns list of values
"""
print("Values Method")
print(person1.values(), "\n")


"""
setdefault()
dictionary.setdefault(key, default_value) -> returns value if key is present in dict else add the key in dict 
with value as 'None' if optional parameter i.e default_value not passed
"""
print("SetDefault Method")
print(person1.setdefault("name", "Added"))
# As name key present in dict it returns value
print(person1.setdefault("city", "Added"))
# As city key is not present in dict it will add ('city':'Added') in dict and returns 'Added'
print(person1.setdefault("place"), "\n")
# As city key is not present in dict it will add ('city':None) in dict as default_value not provided and return None


"""
update()
dictionary.update(other_dictionary/tuple)
"""
print("Update Method")
new_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
person1.update(new_dict)            # will add new_dict to end of the person1 dict
print(person1, "\n")

