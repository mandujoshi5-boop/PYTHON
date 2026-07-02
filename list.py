#list
'''
names=["Mandar","Hrishant","Gaurav"]
print(names) #it will print the whole list
print(type(names))

empty = []                      # empty list
nums = [1, 2, 3, 4]              # list of integers
mixed = [1, "two", 3.0, True]    # mixed types are allowed
nested = [[1, 2], [3, 4]]        # list of lists

# Using the list() constructor(A constructor help to convert other data types into list)
from_string = list("hello")      # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))      # [0, 1, 2, 3, 4]
from_tuple = list((1, 2, 3))     # [1, 2, 3]
print(from_string)
print(from_range)
print(from_tuple)
'''
colors = ["red", "green", "blue", "yellow", "purple"]

colors[0]      # 'red'        -> first element
colors[-1]     # 'purple'     -> last element
colors[1:3]    # ['green', 'blue']     -> slice [start:stop]
colors[:2]     # ['red', 'green']      -> from start
colors[2:]     # ['blue', 'yellow', 'purple']  -> to end
colors[::-1]   # reversed list
colors[::2]    # every 2nd element -> ['red', 'blue', 'purple']
#list_name[staring_index:ending_index:step] (ending index is not included in the print statement)

#modifying list
nums = [1, 2, 3]

nums[0] = 100              # change an element -> [100, 2, 3]
nums.append(4)             # add to end -> [100, 2, 3, 4]
nums.insert(1, 99)         # insert at index 1 -> [100, 99, 2, 3, 4]
nums.extend([5, 6])        # add multiple items -> [..., 5, 6]
nums.remove(99)            # removes first matching VALUE
popped = nums.pop()        # removes & returns LAST item
popped_at = nums.pop(0)    # removes & returns item at index 0
del nums[0]                # delete by index (no return value)
nums.clear()                # empties the list -> []

#USefull list methods
nums = [5, 3, 1, 4, 2]

nums.sort()              # sorts in place -> [1, 2, 3, 4, 5]
nums.sort(reverse=True)  # descending order
sorted(nums)             # returns a NEW sorted list, original unchanged
nums.reverse()           # reverses in place
nums.count(3)            # how many times 3 appears
nums.index(4)             # index of first occurrence of 4
nums.copy()               # shallow copy

#Q1
'''
colors=["red","green","blue","yellow"]
print(colors)
letter=list(input("enter any word to convert into list:"))
print(letter)
'''
#Q2
'''
num=[10,20,30,40,50]
print(num[0])
print(num[-1])
print(num[2])
'''
#Q3
'''
num=[10,20,30,40,50]
print(num[1:3])
print(num[-5:-1])
'''
nums=input("enter the numbers:")
nums=nums.split(",")
target_numb=int(input("enter the number to find:"))
if nums[0]+nums[1]==target_numb:
    print(nums[0],nums[1])
    if nums[0]+nums[1]!=target_numb:
        nums[0]+=1
else:
    print("no such numbers found")