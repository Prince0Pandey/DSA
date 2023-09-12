high_temp = []
input1 = int(input("How many day's temperature? "))
for i in range(input1):
    input2 = int(input(f"Day {i+1}'s high temperature: "))
    high_temp.append(input2)
print()

Average = round(sum(high_temp) / len(high_temp), 2)
print(f"Average = {Average}")

temp = 0
for temperature in high_temp:
    if temperature > Average:
        temp += 1
print(f"{temp} day(s) above average")
