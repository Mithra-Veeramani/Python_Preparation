# # Employee Information 

# employee_name,employee_age,employee_salary,employee_dept = "MOHAN",26,112080,"IT"
# # employee_age = 21
# # employee_salary = 100000
# # employee_dept = "IT"

# no_of_year_studied = 16
# age = 26
# no_of_year_studied,age = age,no_of_year_studied
# print("no_of_year_studied:",no_of_year_studied)
# print("age:",age)

# # Company Constant 

# COMPANY_NAME = "GeniusJobs"
# WORKING_HOURS = 8

# # Display Employee Information 

# print("Employee Details")
# print("----------------")

# print("Company:",COMPANY_NAME)
# print("Name:",employee_name)
# print("Age:",employee_age)
# print("Salary:",employee_salary)
# print("Department:",employee_dept)
# print("Working Hours:",WORKING_HOURS)
# print("Ageofmohan:",age)
# print("Noofyear:",no_of_year_studied)

# lesson 1.5 Datatypes

# Basic_Data_types
# employee_name = "Mithra" -- String datatype
# employee_age = 26 -- Integer datatype
# employee_salary = 112080.50 -- Float datatype
# is_employee_active = True -- Boolean datatype

# Integer (int) -- An integer represents a whole number without a decimal component.
# age = 26
# employee_count = 100
# salary = 50000
# temperature = -10
# print(type(age))

# Float (float) -- A float represents a number with a fractional component.
# employee_salary = 45000.50
# height = 5.8
# rating = 4.5
# percentage = 85.75
# print(type(employee_salary)),print(type(height)),print(type(rating)),print(type(percentage))

# String (str) -- A string represents text. In Python, strings are written inside quotation marks
# Single quotes ' '
# Double quotes " "
# Triple quotes ''' ''' or """ """
# employee_name = "Mohan"
# department = 'IT'
# company = """GeniusJobs"""
# print(type(employee_name))
# print(type(department))
# print(type(company))

# Boolean (bool) -- A Boolean represents one of two values
# is_employee_active = True
# is_job_available = False
# print(type(is_employee_active))
# print(type(is_job_available))

# Practical exercise — Employee Data Type Checker
# employee_name = "Mithra"
# employee_age = "21"
# employee_salary = 30000.00
# employee_dept = "IT"
# is_employee_active = False

# print("Emp Information")
# print("---------------")

# print("Name:",employee_name,type(employee_name))
# print("Age:",employee_age,type(employee_age))
# print("Salary:",employee_salary,type(employee_salary))
# print("Department:",employee_dept,type(employee_dept))
# print("Active:",is_employee_active,type(is_employee_active))

# Lesson 1.6 Type Conversion

# Type conversion means changing a value from one datatype into another 
# FOR Example: 
# str-->int,int-->float,float-->int,int-->str,int-->boolean
# Integer conversion — int()
        # employee_age = "25"
        # employee_age = int(employee_age)
        # print(employee_age + 5)
# Float conversion — float()
        # employee_salary = "30000.50"
        # salary = float(employee_salary)
        # increment = 5000.50
        # updated_salary = salary + increment
        # print("Updated Salary:", updated_salary)
# String conversion — str()
        # employee_age = 25
        # message = "Employee age: " + str(employee_age)
        # print(message)
# Boolean conversion — bool()
        # print(bool(1)) -->True
        # print(bool(0)) -->False
        # print(bool("Hello")) -->True
        # print(bool("")) -->False
# An important detail: empty strings and empty collections are falsey. Most non-empty values are truthy.


# Practical exercise — Employee Salary Calculator

# employee_name = input("Enter employee name:")
# employee_age = input("Enter employee age:")
# employee_salary = input("Enter employee salary:")

# employee_age = int(employee_age)
# employee_salary = float(employee_salary)

# increment = 5000
# updated_salary = employee_salary + increment

# print("\n Employee Details")
# print("-------------------")

# print(f"Name: {employee_name}")
# print(f"Age: {employee_age}")
# print(f"Previous Salary: {employee_salary}")
# print(f"Updated Salary: {updated_salary}")
# print(type(employee_age))
# print(type(employee_salary))

# Lesson 1.7 -- Input/Output
# Understanding print()--The print() function displays information in the terminal.
# Understanding input()--The input() function accepts information from the user.Remember: input() always returns a string.
# Printing multiple values --Python automatically separates multiple arguments with a space by default.
    # eg:   # name = "Mithra"
            # age = 26
            # city = "Puducherry"
            # print(name, age, city)
# Output : Mithra 26 Puducherry
# Understanding sep -- sep controls the separator between multiple values.
    # eg : print("Mithra", 26, "IT", sep="-") -- Mithra-26-IT
    # eg : print("2026","11","13",sep="/") -- 2026/11/13
# Understanding end -- By default, print() moves to a new line after displaying output but we can change this using end.
    # eg : print("Hello", end=" ")
    #      print("Python") -- Hello Python
#    eg : print("Loading", end="...")
#         print("Completed") -- Loadning...Completed
# Understanding f-strings -- This is one of the most useful features in Python.
# Instead of writing:
# name = "Mithra"
# age = 26
# print("My name is", name, "and my age is", age)

# You can write:

# name = "Mithra"
# age = 26
# print(f"My name is {name} and my age is {age}")
# Output : My name is Mithra and my age is 26