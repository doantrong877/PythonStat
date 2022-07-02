# 1) CountDown
from tkinter import Y


def countDown(x):
    arr = []
    if x < 0:
        return "Invalid"
    if x == 0:
        return [0]
    else:
        for x in range(x, -1, -1):
            arr.append(x)
        return arr
print(countDown(5))

# 2) Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]
print(print_and_return([1,2]))

# 3) First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)
print(first_plus_length([1,2,3,4,5]))

# 4) Value Greater than Second
def values_greater_than_second(arr):
    new_arr = [];
    if len(arr) < 2:
        return False
    for x in range(len(arr)):
        if arr[x] > arr[1]:
            new_arr.append(arr[x])
    return new_arr
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5) This Length, That Value

def length_and_value(x,y):
    arr = []
    for a in range(x):
        arr.append(y)
    return arr
print(length_and_value(4,7))
print(length_and_value(6,2))


