#Tuples
fruits = ("apple", "banana", "cherry")
(fruits)        # ('apple', 'banana', 'cherry')
(type(fruits))  # <class 'tuple'> 

empty = ()                          # empty tuple
single = (42,)                      # single-item tuple — the comma is REQUIRED
single_wrong = (42)                 # NOT a tuple — just the number 42 in brackets
nums = (1, 2, 3, 4)                 # tuple of integers
mixed = (1, "two", 3.0, True)       # mixed types allowed
nested = ((1, 2), (3, 4))           # tuple of tuples

# Without parentheses — tuple packing (Python still creates a tuple)
packed = 1, 2, 3
print(type(packed))   # <class 'tuple'>

# Using the tuple() constructor
from_list = tuple([1, 2, 3])        # [1, 2, 3] -> (1, 2, 3)
from_string = tuple("hello")        # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))        # (0, 1, 2, 3, 4)

#Tuples Are Immutable — What That Means
nums = (1, 2, 3)

nums[0] = 100    # TypeError: 'tuple' object does not support item assignment
nums.append(4)   # AttributeError: 'tuple' object has no attribute 'append'
nums.remove(1)   # AttributeError: 'tuple' object has no attribute 'remove'
del nums[0]      # TypeError: 'tuple' object doesn't support item deletion

#BUT YOU CAN REASSIGN THE VARIABLE
num_s=(1,2,3)
num_s=(1,2,3,4)
print(num_s)