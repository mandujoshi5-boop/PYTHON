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
#dictionary nested list methods
'''
phone_book={
    "jaykishor_singh":1234567890,
    "mandar_joshi":9321654529,
    "hrishant_joshi":9987820570
}
#print(phone_book["hrishant_joshi"])
#print(phone_book.get("gaurav_soni"))
phone_book["gaurav_soni"]=8928263839
#print(phone_book)
phone_book["mandar_joshi"]=9321654525
#print(phone_book)
remove=phone_book.pop("jaykishor_singh")
#print(remove)
del phone_book["gaurav_soni"]
#print(phone_book)

library = {
    "book1": {"title": "Python Crash Course", "author": "Eric Matthes", "pages": 544},
    "book2": {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "pages": 592},
    "book3": {"title": "Deep Learning", "author": "Ian Goodfellow", "pages": 800}
}
#print(library.keys())
#print(library["book3"]["title"])
#for title,pages in library.items():
#print(title, "contains",pages)


# Basic comprehension
squares= {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transform existing dict
prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0}
discounted = {item: price * 0.9 for item, price in prices.items()}
# {'apple': 1.35, 'banana': 0.45, 'cherry': 2.7}

defaults = {"lr": 0.01, "epochs": 10, "dropout": 0.3}
custom   = {"lr": 0.001, "batch_size": 64}
merged = defaults | custom
print(merged)
'''
#In the merging method the second or any other dictonary you merged at last win in the duplicate keys

#defaultdict:-
#defaultdict is just a normal dictionary that automatically sets a default value for any new key, so you never crash on missing keys.
#example
'''
from collections import defaultdict
name_count=defaultdict(int)
names={}
names.update({"mandar":["python","java"],"jaykishor":["c++","java"]})
for name in names:
    name_count[name]+=1
    
print(dict(name_count))
'''
'''
from collections import defaultdict
word_count = defaultdict(int)

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1   # No KeyError — new keys default to 0

print(dict(word_count))
print(type(word_count))
'''

# Counter:-
# counter is a subclass of dict that helps count hashable objects. It counts the number of occurrences of each element in an iterable and returns a dictionary-like object where keys are the elements and values are their counts.
'''
from collections import Counter
words=["apple", "banana", "apple", "cherry", "banana", "apple"]
counts=Counter(words)
print(counts)
'''
#problem statement:-
#P1
'''
students = {
    "Tony"  : 92,
    "Raj"   : 45,
    "Priya" : 78,
    "John"  : 38,
    "Sara"  : 85,
    "Ali"   : 61,
    "Neha"  : 29
}
print(students["Tony"])
print(students.get("Rohan","Student not found"))
students["Tony"]=97
print(students["Tony"])
students.update({"Meera":74})
del students["John"]
print(students)
for name,marks in students.items():
    if marks>=50:
        status="Pass"
    else:
        status="Fail"
    print(name,"->",status)

toppers={name:marks for name,marks in students.items() if marks >= 80}
print(toppers)
'''
#myself={"name":"Mandar","age":17,"city":"Mumbai"}
# print(myself["name"])
# print(myself["age"])
# print(myself["city"])
#students={"Mandar":90,"hrishant":91,"gaurav":92}
# print(students.get("apurv","Student not found"))
'''fruits={"Apple":10,"Banana":30,"Mango":90}
fruits["Mango"]=100
fruits.update({"Grapes":50})
del fruits["Apple"]
print(fruits)'''

#P2
'''
info={"India":"Delhi","USA":"Washington DC","Japan":"Tokyo", "Germany":"Berlin","France":"Paris"}
for country,capital in info.items():
    print(f"{country} -> {capital}")

sentence="the dog sat on the mat the dog"
word_count={}
for word in sentence.split():
    word_count[word]=word_count.get(word,0)+1
print(word_count)

original = {"a": 1, "b": 2, "c": 3}
flipped = {value: key for key, value in original.items()}
print(flipped)
'''
#P3
'''
students={
    "Tony":{
        "Marks":90,"Grade":"A"
    },
    "Raj":{
        "Marks":45,"Grade":"C"
    },
    "Priya":{
        "Marks":78,"Grade":"B"
    }
}
for name,details in students.items():
    print(f"{name} -> Marks: {details['Marks']}, Grade: {details['Grade']}")
'''
'''from collections import defaultdict
people_by_country = defaultdict(list)
people = [("India", "Tony"), ("USA", "John"), ("India", "Priya"), ("USA", "Sara"), ("UK", "Raj")]
for country,name in people:
    people_by_country[country].append(name)
print(dict(people_by_country))'''

students = {"Tony": 92, "Raj": 45, "Priya": 78, "John": 38, "Sara": 85}
toppers={name:marks for name,marks in students.items() if marks>=50}
print(toppers)
