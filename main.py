#variable & values
age = 30
print(age)

friend_age = 30
print(friend_age)

PI = 3.14 #constant value we cannot change it
print(PI)

x = 25 #valid variable
print(x)
age = 30 #integer/whole number
print(age)

age = 25.5 #float number(always with decimal point)
print(25.5)
#numbers
float_divison = 200/10
print(float_divison)

int_divison = 200//10
print(int_divison)

remainder = 13 % 5
print(remainder)

remainder = 340 % 2 #modulus_operator/percent sign
print(remainder)

x = 346
remainder = x % 2 #to check odd/even
print(remainder)

#exercise with numbers
a = 17.5
b = 5
x = a + b - 9
print(x)

friends = 9
near = 3
friends_away = friends - near
print(friends_away)

x = 235
modulus_operator = x % 2
print(modulus_operator)

a = 20
b = 25
str_a = str(a)
str_b = str(b)
print(str_a + str_b)

#strings
scores = "my cgpa in masters is '3.41'"
print(scores)
string= "hello it's me."
print(string)
string = 'hello its me ghouse. "how are you?".'
print(string)
#add names to strings
name = "ghouse"
greeting = ", welcome to python introduction class"
print(name + greeting)

name = "ghouse"
greetings = "welcome to python introduction class " + name
print(greetings)

#adding numbers to strings
age = "24"
statement = "ghouse age is " + age
print(statement)
#adding numbers to strings using str function
age = 24
statement = "ghouse age is " + str(age)
print(statement)

#using input
# First, as the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

user_name = input("enter your name:")
print(f"Hello, {user_name}")

user_age = input("enter your age:")
months = int(user_age * 12)
print(f"the number of months out is {months}")

## Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
user_age = int(input("enter your age:"))
print(user_age * 12)

#boolean comparisions(>=/<=/==)
my_number = 5
user_number = int(input("enter your number:"))
matches = my_number == user_number
print(f"you got it right: {matches}.")

#and/or functions
#and
age = 20
result = age < 20 and age < 26 #true and true
print(result)

#or
age = 25
result = age > 20 or age > 21
print(result)

default_user_name = "there"
name = input("enter your name: (optional)")
user_name = name or default_user_name
print(f"Hello, {user_name}")

x = True
user_input = x and 18
print(user_input)

#What would the output of this code be? Imagine the user enters 16.
age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job) #The conditionals evaluate first, and then `and` and `or` evaluate left to right.


#braces for lists, tuples, sets,
#Lists = [] ["ghouse"],
#tuples = (, ) ("ghouse", )
#Sets = {} {"ghouse", "hasi"}
#dict = {:} {"ghouse": }



#lists with elements
friends = ["jose", "ghouse", "swaroop"]
print(friends[0])
print(friends[2])
print(len(friends))

#more lists in one list- every lists starts with 0,1,2,3....
friends = [["ghouse", 24], ["swaroop", 23], ["sudeer", 25]]
print(friends[2][0][1])

#to add anything to the list we use, .append()
friends = [["ghouse", 24], ["swaroop", 23], ["sudeer", 25]]
friends.append(["hasi", 24])
print(friends)

#to remove anything from the list we use, .remove()
friends = ["ghouse", "swaroop", "sudeer"]
friends.remove("sudeer")
print(friends)

#tuples- if you want to add anything to tuple we cannot use .append()function. we can add directly to the strings.
#in Tuples, we cannot remove any element like lists.
friends = ("bob", "anne", "jose",)
friends = friends + ("ghouse",)
print(friends)

#adding numbers to list
list_number = ["23", "24"]
list_number.append("25")
print(list_number)

#sets
art_friends = {"ann", "jose"}
science_friends = {"victor", "jose"}
#sets_add function
art_friends.add("nick")
print(art_friends)
#sets_remove function
science_friends.remove("jose")
print(science_friends)

friends = ("a", "b", "c", "d", "e", "f")
friends_len = (len(friends))
print(friends_len)

var = "guru"
number = 99
str_number = str(number)
print(var + str_number)

science_friends = {"ann", "jose", "nick"}
arts_friends = {"nick", "rock"}
science_but_not_arts = science_friends.difference(arts_friends)
print(science_but_not_arts)
#not in both function, we use .symmetric_difference()
not_in_both = science_friends.symmetric_difference(arts_friends)
print(not_in_both)
#common among two sets, we use .intersection()
art_and_science = arts_friends.intersection(science_friends)
print(art_and_science)
#print everything in the both sets, we use .union()
all_friends = arts_friends.union(science_friends)
print(all_friends)

nearby_people = {"rolf", "jen", "anna"}
user_friends = set()
user_name = input("enter your name:")
user_friends.add(user_name)
print(user_friends)
print(nearby_people.intersection(user_friends))


#average function using list/tuple/set
grades = [80, 85, 90, 95, 100] #list
grades = (80, 85, 90, 95, 100) #tuple
grades = {80, 85, 90, 95, 100} #set
#which function is best to use among this?
# list - we can add new values to it
#tuple - we cannot add new values
# set - we cannot add same values/duplicates because it will remove one.

#average function using list
grades = [80, 85, 90, 95, 100]
total = sum(grades)
lenght = len(grades)

average = total / lenght
print(average)

#join function in list
friends = ["rolf", "ann", "nick"]
comma_separated = ", ".join(friends)
print(f"my friends are {comma_separated}")


#dictionaries print it as dict()
#using symbol dict = {}
#syntax = {"a": A, "b": B} here "a" = key A = value
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print (Dict['Tiffany'])
#copying method of dictionary
dict = {'ghouse': 24, 'swaroop': 23, 'sudeer': 25, 'haseena':24}
boys = {'ghouse': 24, 'swaroop': 23, 'sudeer': 25}
girls = {'haseena': 24}
x = boys.copy()
y = girls.copy()
print(x)
print(y)
#updating method of dictionary
dict = {'ghouse': 24, 'swaroop': 23, 'sudeer': 25, 'haseena':24}
dict.update({'ann': 25})
print(dict)
# delete
dict = {'ghouse': 24, 'swaroop': 23, 'sudeer': 25, 'haseena':24}
del dict['ghouse']
print(dict)
#length function
dict = {'ghouse': 24, 'swaroop': 23, 'sudeer': 25, 'haseena':24}
print(len(dict))

my_friends = {
    'Jose': {'last_seen': 6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}
print(['jose']['last_seen'])

#if syntax = if user_name == friend_name:
#we need to give 4 spaces to print() = indentation
name = "rolf"
user_name = input("enter your name:")
if user_name == name: #if your statement is true then it will print if statement.
    print("hello, friend!")
else: #if statement is not true it will jump to else
    print("hello, stranger!")


friends = ["ghouse", "swaroop", "sudeer"]
family = ["shareef", "hasina"]
user_name = input("enter your name: ")
if user_name in friends: #we used in function insted of ==
    print("hello, friend!")
elif user_name in family: # elif function can do similar to else function
    print("hello, family member! ")
else:
    print("i don't know who you're! ")

#example of if
rolf = 35
steven = 29
if rolf > steven:
    print("rolf is older than steven. ")


#if statements using input, elif, else.

friends = ["rolf", "jen", "steven"]
family_friends = ["ghouse", "swaroop"]
user_name = input("enter your name: ")
if user_name in friends:
    print("hello, my dear friend!")
elif user_name in family_friends:
    print("hello, family_freind")
else:
    print("hello, stranger! i don't know who you are? ")


friends = {"ghouse": 24, "swaroop": 24, "sudeer": 25}
for name, age in friends.items():
    print(f"{name} is {age} years old!")


i = 0
while i < 10:
    print(f"repeated {i} number of times.")
    i += 1

#while & for loops

#while loop
user_input = input("do want to run the program? (p/q) ")
p = "run the program "
q = "quit the program "
user_typed = ["p"]

while user_input == "p":
    print("hello")
    user_input = input("do you want to run the program? (p/q) ")
    print("programme stopped")
    if user_input in user_typed:
        print("Hello")
    else:
        print("not hello")


#for loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#using range function in for loop
for index in range(2, 20):
  print(index)

#example for for loop
student_name_grades = [
    {"name" : "ghouse", "grade" : 95},
    {"name" : "swaroop", "grade" : 97},
    {"name" : "sudeer", "grade" : 100},
]

for student in student_name_grades:
    name = student ["name"]
    grade = student ["grade"]
    print(f"{name} has grade of {grade}.")


#destructuring sytax
friends = [("ghouse", 24), ("swaroop", 25), ("sudeer", 25)]
for name, age in friends:
    print(name, age)
#another way is using f_formating
family = [("ghouse", 24), ("hasina", 24)]
for name, age in family:
    print(f"{name} age is {age}")

#another way
friends = [("ghouse", 24), ("swaroop", 24), ("sudeer", 25)]
for name, age in friends:
    print(f"{name} is {age} years old")

#iterating using for loop
friends = {"ghouse": 24, "swaroop": 24, "sudeer": 25}
for name, age in friends.items():
    print(f"{name} is {age} years old!")


#stnax python
print(type(1)) # int
print([1, 2, 3]) #list
(1, 2, 3) #tuple
{1, 2, 3} #set
False #Bool
2.3 #Float
{1:2} #dict
#if : #if statement
#while : #while loop
strings = "hello world" #strings

# break in for loop
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("stopping the production")
        break
    print(f"car conditon is {status}")

# continue function in for loop
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("stopping the production, skipping...")
        continue
    print(f"car condition is {status}.")
    print("we can ship it to constumers.")

# example #here's how you can use a for loop with range() to repeat something a certain number of times:
for i in range(20):
    print(i)

# example
kid_ages = [3, 7, 12]
for age in kid_ages:
    print(age)

# example of while loop
i = 0
while i < 10:
    print(f"repeated {i} number of time.")
    i += 1

# The FizzBuzz challenge
# In this exercise, print out 100 numbers, from 1 to 100 (both inclusive). But:
# Instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("num")


