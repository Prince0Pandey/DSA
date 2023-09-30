# Q-4. What will be the output of the following code snippet?
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
"""
A. 1 44
B. 3 1
C. 3 44
D. 1 1
"""


# Q-6. What will be the output of the following code snippet?
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))
"""
A. 1
B. 2
C. 3 
D. 4
E. 5
F. 6
"""


# Q-7. What will be the output of the following code snippet?
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
"""
A. 1 2 3 4
B. 1 4 8 12
C. 4 7 11 15 
D. 12,13,14,15
"""

# Q-8. What will be the output of the following code snippet?


def f(j, values=[]):
    values.append(j)
    print(values)
    return values
f(1)
f(2)
f(3)
"""
A. [1] [2] [3]
B. [1, 2, 3]
C. [1] [1, 2] [1, 2, 3]
D. 1 2 3
"""