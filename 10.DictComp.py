"""
DICTIONARY COMPREHENSION SYNTAX
new_dict = {key: value for (key, value) in dict.items() if condition}
"""
import random

city_names = ["mumbai", "pune", "surat", "chandigarh", "gurgaon"]

city_temps = {key: random.randint(20, 30) for key in city_names}
print(city_temps)

above25 = {city: temp for (city, temp) in city_temps.items() if city_temps[city] > 25}
print(above25)

