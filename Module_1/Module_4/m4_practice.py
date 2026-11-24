# Module -- 4 
# Lesson 1.1 String
# company = "GENIUSJOBS"
# 0,1,2,3,4,5,6,7,8,9 -- Positive indexing
# -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 -- negative indexing 
# print(company[0])
# print(company[-1])
# print(company[0:4])
# print(company[6:10])

# 1.2 String METHOD

# 1.lower () -- Converts all characters to lowercase.
# 2.Upper () -- Converts all characters to Uppercase.
# 3.Strip () -- Removes whitespace from the beginning and end of a string.
# 4.replace () -- Replaces a particular substring with another.
# 5.split () -- Splits a string into a list.
# 6.join () -- Combines multiple strings into one string using a separator.

# candidate_name = "   mithra veeramani   "
# skills = "Python,Java,React,SQL"

# cleaned_name = candidate_name.strip()
# print(cleaned_name.upper())

# updated_skills = skills.replace("Java", "JavaScript")
# print(updated_skills)

# skills_list = updated_skills.split(",")
# print(skills_list)

# print(" | ".join(skills_list))

# 1.3 String Formating -- String formatting allows us to insert variables and expressions inside strings.

# student_name = "Mithu"
# subject = "Python"
# marks = 87
# total_marks = 100

# percentage = (marks / total_marks) * 100

# print(f"Student Name: {student_name}")
# print(f"Subject: {subject}")
# print(f"Marks: {marks}/{total_marks}")
# print(f"Percentage: {percentage:.2f}%")

# Strings — Lesson recap
# You've covered:
# 1. Single, double and triple quotes.
# 2. Positive and negative indexing.
# 3. String slicing.
# 4. lower(), upper(), strip(), replace(), split(), join().
# 5. String immutability.
# 6. String formatting using f-strings.

# Lists 
# 1.What is a list?
# A list is a collection used to store multiple values in a single variable.
# 2.Characteristics of lists
# - Ordered: Items maintain their positions.
# - Mutable: You can modify items after creation.
# - Allows duplicates: The same value can appear multiple times.
# - Allows different data types: Strings, integers, floats, and booleans can coexist.
# 3.Accessing list elements
# - Lists use indexing, just like strings.
# 4.Updating list elements
#  - Because lists are mutable, you can change an existing item.
# 5.List slicing
#  - The syntax is the same as string slicing

# eg:

# employees = ["Rahul", "Priya", "Ananya", "Mohan"]
# employees[1] = "Mithu"

# print(employees[0])
# print(employees[-1])
# print(employees)
# print(employees[0:3])

# # Adding elements to a list -- Python provides three important methods.
# # 1. append() — Add one item at the end
# # 2. extend() — Add multiple items
# # 3. insert() — Add an item at a specific position

# Important difference between append() and extend():

# numbers = [1, 2]numbers.append([3, 4])
# print(numbers)

# Output: [1, 2, [3, 4]]

# But:

# numbers = [1, 2]numbers.extend([3, 4])
# print(numbers)

# # Output: [1, 2, 3, 4]

# # append() adds the entire list as one element. extend() adds its elements individually.

# employees = ["Rahul", "Priya"]

# # Add one employee
# employees.append("Mithu")

# # Add multiple employees
# employees.extend(["Ananya", "Anandh"])

# # Insert at index 1
# employees.insert(1, "Kumar")

# # Display final list
# print(employees)

# Removing elements from a list -- Python provides three important methods.

# 1. remove() — Remove by value
# 2. pop() — Remove by index
# Important: pop() also returns the removed element.
# removed_employee = employees.pop(1)
# print(removed_employee)
# Output: Priya
# 3. clear() — Remove everything

# employees = ["Rahul", "Priya", "Mithu", "Ananya", "Vinoth"]

# employees.remove("Priya")
# removed_employees = employees.pop(3)
# print(removed_employees)

# print(employees)

# Sorting, reversing, counting and finding items 

# 1. sort() — Sort items
# 2. reverse() — Reverse the current order -- Note: reverse() does not sort. It simply reverses the existing order.
# 3. count() — Count occurrences
# 4. index() — Find the position -- If the value doesn't exist, index() raises a ValueError.

# numbers = [50, 20, 40, 20, 10, 30]

# # Sort in ascending order
# numbers.sort()
# print(numbers)

# # Reverse the list
# numbers.reverse()
# print(numbers)

# # Count occurrences of 20
# print(numbers.count(20))

# # # Find index of 40
# # print(numbers.index(40))

# # list comprehension.
# # Syntax : new_list = [expression for item in iterable]

# # normal: 
# numbers = [1, 2, 3, 4, 5]

# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)
# # list comprehension -- method
# numbers = [1,2,3,4,5,6,7]

# squares = [number ** 2 for number in numbers]
# print(squares)

# List comprehension with conditions

# You can also filter values while creating a new list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]
# Syntax:new_list = [expression for item in iterable if condition]
# eg: 
# numbers = [1, 2, 3, 4, 5]
# result = [number * 10 for number in numbers if number > 2]
# print(result) -- o/p -- 30,40,50

# Module 4.3 — Tuples
# 1. What is a tuple?
# A tuple is a Python data structure used to store multiple values in a single variable.

# It is similar to a list, but the main difference is:
# - List → Mutable (can be modified).
# - Tuple → Immutable (cannot be modified after creation).
# the difference in brackets:
# - Lists use [].
# - Tuples use ().

# 2. Creating tuples -- Tuples can store different data types (-- Strings --Integers -- Floats -- Booleans -- Even other collections)
# student = ("ST101", "Mithu", 85, True)
# print(student)

# 3. Accessing tuple elements
# Just like lists and strings, tuples support positive and negative indexing

# 4. Tuple slicing
# # Tuples also support slicing.

# 5. Tuple immutability
# This is the most important characteristic of tuples.
# Look at this example:
# employees = ("Rahul", "Priya", "Mithu")
# employees[1] = "Ananya"
# print(employees)

# Python raises:
# TypeError: 'tuple' object does not support item assignment
# Why?
# Because tuples are immutable. You cannot change, add, or remove individual elements after creating a tuple.

# Compare:
# Listemployees = ["Rahul", "Priya"]
# employees[1] = "Mithu"  # Allowed# 
# Tupleemployees = ("Rahul", "Priya")
# employees[1] = "Mithu"  # Error

# 6. Single-element tuple
# This is a common interview question.

# Look at these examples:
# a = ("Python")
# b = ("Python",)
# print(type(a))
# print(type(b))

# Output:
# <class 'str'>
# <class 'tuple'>
# Why?
# - ("Python") is simply a string inside parentheses.
# - ("Python",) is a tuple because it has a trailing comma.
# Remember: The comma creates a single-element tuple, not the parentheses alone.

# 7. Tuple unpacking
# Tuple unpacking means assigning tuple elements to separate variables in one statement.

# Example:
# employee = ("Mithu", 25, "Developer")
# name, age, profession = employee
# print(name)
# print(age)
# print(profession)

# Output:
# Mithu
# 25
# Developer

# Python automatically assigns:
# - First element → name
# - Second element → age
# - Third element → profession
# The number of variables must match the number of tuple elements for ordinary unpacking.

# 8. When should you use tuples instead of lists?
# Situation	Recommended
# Employee names that frequently change	List
# Fixed employee record fields	Tuple
# Collection that needs adding/removing items	List
# Fixed coordinates (x, y)	Tuple
# Values that should not be reassigned individually	Tuple

# One important detail: a tuple prevents changing its own elements, but if it contains a mutable object such as a list, that inner list can still be modified.

# employee = ("Mithu", 25, "Python Developer", 35000)

# print(employee[0])
# print(employee[-1])
# print(employee[0:3])

# name,age,profession,salary = employee
# print(name)
# print(age)
# print(profession)
# print(salary)

# Lesson 4.3 — Tuples completed
# You've understood:
# - Tuple creation and accessing elements.
# - Positive and negative indexing.
# - Slicing.
# - Immutability.
# - Single-element tuple syntax.
# - Tuple unpacking.
# - Choosing tuples over lists.

# Lesson 4.4  Sets

# What is a set? -- A set is a Python data structure used to store unique elements.
    # The most important characteristic is that sets do not allow duplicate values.
# employees = {"Rahul", "Priya", "Mithu", "Rahul"}
# print(employees) -- {'Rahul', 'Priya', 'Mithu'}

# Creating a set
    # numbers = {10, 20, 30, 40}
    # print(numbers)
    # print(type(numbers))
    # Output:
    # {10, 20, 30, 40}
    # <class 'set'>
# Important: An empty {} creates a dictionary, not a set.

# To create an empty set:
    # empty_set = set()
    # print(type(empty_set))
    # Output:
    # <class 'set'>

# 1.Adding elements — add() -- Use add() to insert one element.
# 2.Removing elements -- Python provides two commonly used methods.
    # skills = {"Python", "Java", "React"}
    # skills.remove("Java")
    # print(skills)
# Removes the specified element. If it doesn't exist, Python raises a KeyError.
    # skills = {"Python", "Java", "React"}
    # skills.discard("PHP")
    # print(skills)
# Does not raise an error if the element doesn't exist.

# 3. Set operation 
# Example:
    # A = {1, 2, 3, 4}
    # B = {3, 4, 5, 6}
# A.Union -- union() -- Symbol: (A U B)
    # print(A.union(B)) -- {1,2,3,4,5,6}
# B. Intersection — intersection() -- Returns only the common elements -- Symbol: (A intersection B)
    # print(A.intersection(B)) -- {3,4}
# C. Difference — difference() -- Returns elements present in the first set but not the second -- 
    # print(A.difference(B)) -- {1,2}
# Reverse the order:
#     print(B.difference(A)) -- {5,6}
# D. Symmetric difference — symmetric_difference() -- Returns elements that exist in either set, but not in both.
    # print(A.symmetric_difference(B)) -- {1,2,5,6}
# It excludes the common elements 3 and 4.

# Your practical exercise

# python_skills = {"Python","SQL","Django","Git"}
# js_skills = {"Js","React","SQL","Git"}

# print(python_skills.union(js_skills))
# print(python_skills.intersection(js_skills))
# print(python_skills.difference(js_skills))
# print(python_skills.symmetric_difference(js_skills))

# python_skills.add("Docker")
# print(python_skills)

# python_skills.remove("Django")
# print(python_skills)

# 4.4 Completed — Sets
# You've learned:
# - Creating sets and removing duplicates.
# - add(), remove(), discard().
# - Union, intersection, difference.
# - Symmetric difference.
# - Why sets don't support indexing.

# 4.5 — Dictionaries
# This is an important topic for backend development because dictionaries store information using key-value pairs.
#  creating a dictonary there are 2 common way 
# Method 1: Using curly braces {}
# Example : 
    # employee = {
    #     "id": 101,
    #     "name": "Mithu",
    #     "role": "Python Developer",
    #     "salary": 35000
    # }
    # print(employee)
# Method 2 : Using dict ()
# Example :
# student = dict(
#     id = "101",
#     name ="Mohan",
#     marks = 90
#  )

# Accessing dictionary values
# There are two methods we will study.
# Method 1: Using square brackets
# Syntax:
# dictionary_name["key"]
# First example: Accessing values
    # print(employee["name"])
    # print(employee["salary"])
# Output:
# Mithu
# 35000
# Python looks for the specified key and returns its corresponding value.

# Practice Exercise :

# employee = {
#     "id": 105,
#     "name" : "Mithra",
#     "role" : "Python Developer",
#     "salary" : 35000,
#     "department" :"IT"
# }
# print(employee)
# print(employee["name"])
# print(employee["salary"])
# print(employee["department"])
# print(type(employee))

# 4.5 Adding dictionary items -- Dictionaries are mutable, so we can add new key-value pairs after creating them.

# 1. Adding a new key-value pair
# Syntax:
    # dictionary_name["new_key"] = value

# Example : 

    # employee = {
    #     "id": 105,
    #     "name": "Mithra",
    #     "salary": 35000
    # }

    # employee["department"] = "IT"
    # print(employee)

# 2. Updating an existing value -- You can use exactly the same syntax to update an existing key.

    # employee = {
    #     "id": 105,
    #     "name": "Mithra",
    #     "salary": 35000
    # }

    # employee["salary"] = 45000
    # print(employee)

# Practice Exercise 

# employee = {
#     "id": 505,
#     "name": "Mithra",
#     "role":"Python Developer",
#     "salary": 35000,
#     "department" : "IT"
# }
# employee["experience"] = 2
# employee["location"] ="Pondicherry"
# employee["salary"] = 45000
# employee["role"] = "Senior Python Developer"
# print(employee)

# 3.Deleting dictionary items -- Python provides three important methods/statements.
# 1. pop() — Remove a specific key
# eg : 
    # employee = {
#     "id": 505,
#     "name": "Mithra",
#     "salary": 45000
# }
# removed_salary = employee.pop("salary")
# print(removed_salary)
# print(employee)

# Output:
# 45000
# {'id': 505, 'name': 'Mithra'} -- Important: pop() removes the key-value pair and returns the removed value.

# 2. del — Delete a specific key
# eg :
    # employee = {
    #     "id": 505,
    #     "name": "Mithra",
    #     "salary": 45000
    # }
    # del employee["salary"]
    # print(employee)
# Output: {'id': 505, 'name': 'Mithra'} -- Unlike pop(), del does not return the removed value.\

# 3. clear() — Remove everything
# eg : 
    # employee = {eg
    #     "id": 505,
    #     "name": "Mithra",
    #     "salary": 45000
    # }
    # employee.clear()
    # print(employee)
# Output: {} -- The dictionary still exists, but it is empty.

# Practical Exercise 

# employee = {
#     "id": 505,
#     "name": "Mithra",
#     "role": "Python Developer",
#     "salary": 45000,
#     "department": "IT"
# }

# removed_salary = employee.pop("salary")
# del employee["department"]
# print(removed_salary)
# print(employee)

# Accessing dictionary values safely with get() -- This is important when working with real application data.

# Using get()
    # Syntax:
    # dictionary.get("key")

# Example:
    # employee = {    
    # "id": 505,    
    # "name": "Mithra",    
    # "salary": 45000
# }
    # print(employee.get("name"))
    # print(employee.get("department"))
# Output:
# Mithra
# None
# Notice the difference:
    # - employee["department"] → raises KeyError.
    # - employee.get("department") → returns None by default.
# Providing a default value -- You can specify what Python should return when the key doesn't exist.
# print(employee.get("department", "Not Available"))
# Output:
# Not Available -- This is useful when displaying incomplete employee profiles.

# employee = {
#     "id": 505,
#     "name": "Mithra",
#     "role": "Python Developer",
#     "salary": 45000
# }
# print(employee.get("name"))
# print(employee.get("salary"))
# print(employee.get("department"))
# print(employee.get("department","Not Available"))

# keys(), values(), and items() -- These three methods help us retrieve different parts of a dictionary.
# employee = {
#     "id": 505,
#     "name": "Mithra",
#     "role": "Python Developer",
#     "salary": 45000
# }
# 1. keys() — Get all keys
# print(employee.keys())
# Output:
# dict_keys(['id', 'name', 'role', 'salary'])
# 2. values() — Get all values
# print(employee.values())
# Output:
# dict_values([505, 'Mithra', 'Python Developer', 45000])
# 3. items() — Get key-value pairs
# print(employee.items())
# Output:
# dict_items([
#     ('id', 505),
#     ('name', 'Mithra'),
#     ('role', 'Python Developer'),
#     ('salary', 45000)
# ])
# Notice that items() gives each key-value pair as a tuple.

# Example: 
# employee = {
#     "id": 505,
#     "name": "Mithra",
#     "role": "Python Developer",
#     "salary": 45000
# }
# print(employee.keys())
# print(employee.values())
# print(employee.items())

# 4.5 — Looping through dictionaries
# This is important because in real projects, we often need to display every employee record or every student's details.
# 1. Loop through dictionary keys
# employee = {    
#             "id": 505,    
#             "name": "Mithra",    
#             "role": "Python Developer",    
#             "salary": 45000}
#         for key in employee:    
#             print(key)

# Output:
# id
# name
# role
# salary
# Why? When you directly loop through a dictionary, Python gives you its keys by default.

# 2. Loop through dictionary values
# for value in employee.values():    
#     print(value)

# Output:
# 505
# Mithra
# Python Developer
# 45000

# 3. Loop through keys and values together --This is where items() becomes useful.
# for key, value in employee.items():    
#     print(key, ":", value)

# Output:
# id : 505
# name : Mithra
# role : Python Developer
# salary : 45000

# Understand this line carefully:
# for key, value in employee.items():
# - employee.items() returns key-value pairs as tuples.
# - key receives the first element.
# - value receives the second element.
# - This is called tuple unpacking.

# PRACTICE EXERCISE 

# student = {
#     "id": "ST101",
#     "name": "Ananya",
#     "course": "Python",
#     "marks": 85,
#     "result": "Pass"
# }
# for key,value in student.items():
#     print(key ,":",value)

# 3. Mutable vs Immutable
# Data type	Mutable or Immutable?
# List	Mutable
# Dictionary	Mutable
# Set	Mutable
# String	Immutable
# Integer	Immutable
# Float	Immutable
# Tuple	Immutable

# Next concept: Creating a separate copy
# numbers = [10, 20, 30]

# another_numbers = numbers.copy()

# another_numbers[1] = 100

# print(numbers)
# print(another_numbers)

# a = [1, 2, 3]
# b = a.copy()

# b.append(4)

# print(a)
# print(b)

# Next: Mutable objects inside functions


# students = {
#     "ST101": {
#         "name": "Mithra",
#         "marks": 85
#     },
#     "ST102": {
#         "name": "Ananya",
#         "marks": 90
#     },
#     "ST103": {
#         "name": "Arjun",
#         "marks": 85
#     },
#     "ST104": {
#         "name": "Mohana",
#         "marks": 95
#     },
#     "ST105": {
#         "name": "Priya",
#         "marks": 88
#     },
#     "ST106": {
#         "name": "Rahul",
#         "marks": 92
#     },
#     "ST107": {
#         "name": "Anandh",
#         "marks": 80
#     }
# }

# # Display all student records
# print("ALL STUDENT RECORDS")
# print("-------------------")

# for student_id, student in students.items():
#     print("Student ID:", student_id)
#     print("Name:", student["name"])
#     print("Marks:", student["marks"])

#     if student["marks"] >= 40:
#         print("Result: Pass")
#     else:
#         print("Result: Needs Improvement")

#     print("-------------------")

# # Search student by ID
# student_id = input("Enter student ID: ").strip().upper()

# student = students.get(student_id)

# if student:
#     print("\nStudent Details")
#     print("-----------------")
#     print("ID:", student_id)
#     print("Name:", student["name"])
#     print("Marks:", student["marks"])

#     if student["marks"] >= 40:
#         print("Result: Pass")
#     else:
#         print("Result: Needs Improvement")
# else:
#     print("Student not found")

