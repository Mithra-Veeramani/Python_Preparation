# What is a function?
# A function is a reusable block of code that performs a specific task.Instead of writing the same code repeatedly, we can write it once inside a function and execute it whenever needed.

# Syntax:
#     def welcome():
#     print("Welcome to Python!")
# welcome()
# Example:
# def display_profile():
#     print("EMPLOYEE PROFILE")
#     print("----------------")
#     employee_detail = {
#         "name": "Mithra",
#         "role": "Python Developer",
#         "department": "IT"
#     }
#     print(f"Name: {employee_detail['name']}")
#     print(f"Role: {employee_detail['role']}")
#     print(f"Department: {employee_detail['department']}")
# display_profile()

# def display_employee():
#         print("Name: Mithra")
#         print("Role: Python Developer")
# def display_company():
#     print("Company: GeniusJobs")
#     print("Industry: IT")
# display_employee()
# display_company()
# display_employee()
# display_company()

# lesson 5.3 Parameters and Arguments
# A parameter is a variable written inside the parentheses when defining a function.
# Parameter --> Variable in function definition
# Argument --> Value passed to the function when calling it

# Example:
# def display_student(name,marks):
#     print("Student Name:", name)
#     print("Student Marks:", marks)
# display_student("Mithra", 95)
# display_student("Mohan", 98)

# def calculate_total(price,quantity):
#     total_salary = price * quantity
#     return total_salary
# total = calculate_total(500, 3)
# print("Total Price:", total*3)

# def calculate_salary(basic_salary, bonus, deduction):
#     final_salary = basic_salary + bonus - deduction
#     return final_salary

# salary = calculate_salary(30000, 5000, 2000)
# print("Final Salary:", salary)

# Lesson : 5.5 — Default Arguments in Python
# A default argument is a value assigned to a function parameter when defining the function.
# If the user doesn't provide a value for that parameter during the function call, Python automatically uses the default value.

# Example :
# def greet_user(name="Guest"):
#     print(f"Hello, {name}")
# greet_user()
# greet_user("Mithra")
# greet_user("Mohan")

# def display_employee(name,department="IT"):
#   print("Employee Name:",name)
#   print("Department:",department)
# display_employee("Mithra");
# display_employee("Mohan","HR");
# display_employee("Anandh");

# Lesson : 5.6 — Positional and Keyword Arguments in Python

# 1. Positional arguments
# Positional arguments are assigned to parameters based on their position (order).
# Python matches the first argument with the first parameter, second with second, and so on.
# if we changed the order the values are assigned incorrectly.

# def display_employee(name, role, salary):
#     print("Name:", name)
#     print("Role:", role)
#     print("Salary:", salary)

# display_employee("Mithra", "Python Developer", 45000)

# 2. Keyword arguments
# Keyword arguments are passed using the parameter names.

# def display_employee(name, role, salary):
#     print("Name:", name)
#     print("Role:", role)
#     print("Salary:", salary)

# display_employee(
#     salary=45000,
#     name="Mithra",
#     role="Python Developer"
# )
# We changed the argument order, but the output is still correct.Because Python matches the values using the parameter names.

# Practice Exercise 1:

# def order_details(product_name,quantity,price):
#     total_price = quantity * price
#     print("Product Name:", product_name)
#     print("Quantity:", quantity)
#     print("Total Price:", total_price)
# order_details("Laptop", 2, 50000)
# order_details(
#     product_name="Mouse",
#     quantity=3,
#     price=500
# )
# order_details("Keyboard", quantity=1, price=1500)

# Next: 5.7 — Variable-Length Arguments
# What is *args?
# *args allows a function to accept multiple positional arguments without specifying the number of parameters in advance.

# def cal_total(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# result1 = cal_total(10, 20, 30)
# result2 = cal_total(100, 200, 300, 400)
# result3 = cal_total(5, 10, 15, 20, 25)
# print("Total 1:", result1)
# print("Total 2:", result2)
# print("Total 3:", result3)

# What is **kwargs?
# **kwargs allows a function to accept multiple keyword arguments without knowing how many arguments will be passed.
# Python collects these arguments into a dictionary.


# def employee_details(**kwargs):
#     print(kwargs)
# employee_details(
#     name="Mithra",
#     role="Python Developer",
#     salary=45000
# )
# # 2. Accessing values inside **kwargs
# def employee_details(**kwargs):
#     print("Name:", kwargs["name"])
#     print("Role:", kwargs["role"])
#     print("Salary:", kwargs["salary"])
# employee_details(
#     name="Mithra",
#     role="Python Developer",
#     salary=45000
# )
# # 3. Looping through **kwargs
# def employee_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# employee_details(
#     name="Mithra",
#     role="Python Developer",
#     salary=45000,
#     department="IT"
# )
# # Practice Exercise 2:
# def student_details(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# student_details(
#     name="Ananya",
#     age=21,
#     course="Python Programming",
#     marks=95,
#     city="Bangalore"
# )

# what is scope in python?
    # Scope means the area of a program where a variable is accessible.
# They are mainly two types of scope in Python:
    # Local Scope/Function Scope: Variables defined inside a function are accessible only within that function.
        # def display_employee():
        #     name = "Mithra"
        #     print("Employee Name:", name)
        # display_employee()
    # Global Scope: Variables defined outside any function are accessible from anywhere in the program.
        # company = "GeniusJobs"
        # def display_company():
        #     print("Company:", company)
        # display_company()
        # print(company)
#To modify the global variable using a keyword global inside a function.
        # salary = 40000
        # def update_salary():
        #   global salary
        #   salary = 45000
        # update_salary()
        # print("Updated Salary:", salary)
# Lambda Functions in Python
# A lambda function is a small anonymous function (a function without a regular name) written in a single expression.
# Syntas:
#   lambda arguments: expression
# 
# Regular function:
    # def square(number):
    #     return number * number
    # print(square(5))

# Lambda function:
    # square = lambda number: number * number
    # print(square(5))
# Regular function and lambda function using map() function
# Syntax:
#   map(function, iterable)
# example:
# # salaries = [20000,25000,30000,35000]
# updated_salaries = map(lambda salary:salary + 5000,salaries)
# print("Original Salaries:", salaries)
# print("Updated Salaries:", list(updated_salaries))


# monthly_salaries = [50000,60000,70000,80000]

# def updated_salaries(salary):
#   return salary + 5000
# new_salary = map(updated_salaries,monthly_salaries)
# print("Original Salaries:", monthly_salaries)
# print("Updated Salaries:", list(new_salary))
#
# Lambda Functions – filter() in Python
# Regular function and lambda function using filter() function
#   filter() is a built-in Python function used to select specific elements from an iterable based on a condition.
# Syntax:
#   filter(function, iterable)
#
# Using filter() with a regular function
#
# salaries = [15000, 25000, 30000, 45000, 60000]

# def check_salary(salary):
#   return salary >= 30000
# result = filter(check_salary,salaries)
# print("Original Salaries:",salaries)
# print("Checked_salaries",list(result))

# Using filter() with a lambda function

# monthly_salaries = [15000, 25000, 30000, 45000, 60000]
# result = filter(lambda salary : salary >= 30000,monthly_salaries)
# print("Original Salaries:",monthly_salaries)
# print("Checked_salaries",list(result))
#
# Module 5.7 Basic Recursion in Python
# In recursion, a function calls itself repeatedly until a particular condition is satisfied.
# Every recursive function needs a stopping condition.
# Each recursive call should move towards that stopping condition.
# Too many recursive calls can cause a RecursionError.
# 
# Practice Exercise 3:
# print("SIMPLE CALCULATOR")
# print("=================")
# def addition(a,b):
#   return a+b
# def subtraction(a,b):
#   return a-b
# def multiplication(a,b):
#   return a*b
# def division(a,b):
#   if b == 0:
#     return "cannot divided by zeroo"
#   return a/b

# num1 = int(input("Enter First number: "))
# operator = input("Enter operator (+,-,*,/): ")  
# num2 = int(input("Enter First number: "))

# if operator == "+":
#   result = addition(num1,num2)
# elif operator == "-":
#   result = subtraction(num1,num2)
# elif operator == "*":
#   result = multiplication(num1,num2)
# elif operator == "/":
#   result = division(num1,num2)
# else:
#   result = "Invalid Operator"

# print("Result:",num1,operator,num2,"=",result)
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
