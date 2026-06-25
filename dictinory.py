#what is dictionary
#dictinory is the mutable collection of the key-value pairs of info 
#In dictionry there is no index no system 
 
'''
eg
person = {"name": "Alice", "age": 30, "city": "Mumbai"}
print(person)          # {'name': 'Alice', 'age': 30, 'city': 'Mumbai'}
print(type(person))    # <class 'dict'>
'''
#creating dictionary
'''
empty = {}                              # empty dictionary
empty = dict()                          # also empty, using constructor

person = {"name": "Alice", "age": 30}   # string keys
nums = {1: "one", 2: "two", 3: "three"} # integer keys
mixed_keys = {"name": "Bob", 1: True}   # mixed key types (allowed)

# Using the dict() constructor
person = dict(name="Alice", age=30)     # keyword argument style
person = dict([("name", "Alice"), ("age", 30)])  # from list of tuples

# Nested dictionary
student = {
    "name": "Alice",
    "grades": {"math": 95, "science": 88},
    "hobbies": ["reading", "coding"]
}
'''

#Value Assignmenet Operation
'''
person = {"name": "Alice", "age": 30, "city": "Mumbai"}

# By key — square bracket notation
print(person["name"])    # Alice

# Using .get() — safer, returns None if key doesn't exist (no error)
print(person.get("age"))         # 30
print(person.get("salary"))      # None
print(person.get("salary", 0))   # 0 -> default value if key missing
'''
#Modifying the Dictionary
'''
person={"name":"Mandar","age":17} #created the dictionary of perion info
person["city"]="Mumbai"           #used to add the new key-value in the dictionary
person["age"]=18                  #used to update the key with assinging new value
person.update({})                 #used to update the multiple values
person.clear()                    #it empty the whole dictionary 
del person["city"]                #it deleted the key with no return value 
'''
#Dictionary Methods

