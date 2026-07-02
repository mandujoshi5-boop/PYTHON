#Negative slicing:-
fruits = "apple,banana,mango"

print(fruits[-1])      # 'o' — the last character
print(fruits[-6:])     # 'mango' — everything from the 6th-last character to the end
print(fruits[:-6])     # 'apple,banana,' — everything except the last 6 characters
print(fruits[-12:-2])  #in the following statement the -2 is not included in print because it start countin from the previous number

filenames = ["report_jan.csv", "report_feb.csv", "report_mar.csv", "report_apr.csv"]
# Reversing a list using a negative step
reversed_list = filenames[::-1]
print(reversed_list)

#stirng functions
str="i am Mandar sachin joshi"
print(str.endswith("joshi")) #it will check wether the string end with joshi or not(print "True")
print(str.capitalize()) #it will capitalize the first letter of the string for once
print(str) #it will not show the capitalized one
# to store in the original first one [str = str.capitalize()]
print(str.replace("a","d")) #it will replace all the "a" with "d" in the string
print(str.replace("Mandar","Mandu")) # it will replace specific string with new one
print(str.find("i")) #it will return the index of the first occurence of the string
print(str.count("s")) #it will return the number of occurences of the string

#Q1
name=input("Enter your name:")
print(len(name))
#Q2
str=input("Enter your full name:")
str1=input("Enter which word you want to count:")
print(str.count(str1))
'''
#if, else & elif statements
#Q1
'''
age=int(input("Enter your age:"))
if (age%2)==0:
    print("your age is even")
else:
    print("your age is odd")
'''
#Q2
'''
num1=int(input("Enter first nummber:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>num2) and (num1>num3):
    print("num 1 is greatest")
elif(num2>num1)and(num2>num3):
    print("num2 is greatest")

'''
#Q3
username=input("Enter your username:")
password=input("Enter your password:")
is_active=True
if username=="Mandar" and password=="09062008":
    if is_active:
        print("login successful")
    else:
        print("account is inactive")
else:
    print("Invalid username or password")
    '''