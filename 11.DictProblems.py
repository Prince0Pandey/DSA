# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for index, (key, value) in enumerate(my_dict.items()):
#     print(f"Index: {index}, Key: {key}, Value: {value}")
"""
COUNT WORD FREQUENCY
Define a function to count the frequency of words in a given list of words.

Example:
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)

Output:{'apple': 3, 'orange': 2, 'banana': 1}
"""
print("Q1. COUNT WORD FREQUENCY")
def count_word_frequency(lst):
    freq = dict()
    value = 1
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = value
    return freq

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words), "\n")
# Time Complexity: O(N)
# Space Complexity: O(N)    N is no. of element in 'freq'


# print("Q1. COUNT WORD FREQUENCY 2nd way using get()")
# def count_word_frequency(words):
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#     return word_count
#
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# print(count_word_frequency(words), "\n")

# Time Complexity: O(N)
# Space Complexity: O(N)

'''
COMMON KEYS & SUM
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

Output:{'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
print("Q2. COMMON KEYS & SUM")
def merge_dicts(dict1, dict2):
    dict3 = dict()
    for key, value in dict1.items():
        if key in dict2:
            dict3[key] = dict1[key] + dict2[key]
        else:
            dict3[key] = value

    for key, value in dict2.items():
        if key not in dict3:
            dict3[key] = value
    return dict3

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2), "\n")
# Time Complexity:  O(M + N) = O(N) where N > M
# Space Complexity: O(N)        N is no. of unique keys in both the dict


# print("Q2. COMMON KEYS & SUM 2nd way using get()")
# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#         result[key] = result.get(key, 0) + value
#     return result
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_dicts(dict1, dict2), "\n")

# Time Complexity:  O(M + N) = O(N) where N > M
# Space Complexity: O(N)        N is no. of unique keys in both the dict


"""
KEY WITH THE HIGHEST VALUE
Define a function which takes a dictionary as a parameter and returns the key with the highest value
in a dictionary.

Example:
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)

Output:b
"""
print("Q3. KEY WITH THE HIGHEST VALUE")
def max_value_key(my_dict):
    max_val = max(my_dict.values())
    for key in my_dict:
        if my_dict[key] == max_val:
            return key
# Time Complexity: O(N)
# Space Complexity: O(1)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict), "\n")


# print("Q3. KEY WITH THE HIGHEST VALUE 2nd way:")
# def max_value_key(my_dict):
#     return max(my_dict, key=my_dict.get)
#
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# print(max_value_key(my_dict), "\n")

# Time Complexity: O(N) because of the max()
# Space Complexity: O(1)


"""
REVERSE KEY-VALUE PAIR
Define a function which takes as a parameter dictionary and returns a dictionary in which every key-value pairs
are reversed.

Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)

Output:{1: 'a', 2: 'b', 3: 'c'}
"""
print("Q4. REVERSE KEY-VALUE PAIR")
def reverse_dict(my_dict):
    reversed_dict = dict()
    for key, value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict), "\n")


# print("Q4. REVERSE KEY-VALUE PAIR 2nd way")
# def reverse_dict(my_dict):
#     return {v: k for k, v in my_dict.items()}
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(reverse_dict(my_dict), "\n")


"""
SAME FREQUENCY
Define a function which takes two lists as parameters and check if two given lists have the same frequency
of elements.

Example:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)

Output:False
"""
print("Q5. SAME FREQUENCY")
def check_same_frequency(lst1, lst2):
    if len(lst1) == len(lst2):
        for element in lst1:
            if element in lst2:
                lst2.remove(element)
        if len(lst1) == len(lst2):
            return True
        else:
            return False
    else:
        return False

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2), "\n")
# Time Complexity: O(N^2)
# Space Complexity: O(1)


# print("Q5. SAME FREQUENCY 2nd way")
# def check_same_frequency(list1, list2):
#     def count_elements(lst):
#         counter = {}
#         for element in lst:
#             counter[element] = counter.get(element, 0) + 1
#         return counter
#
#     return count_elements(list1) == count_elements(list2)
#
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# print(check_same_frequency(list1, list2), "\n")

