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





