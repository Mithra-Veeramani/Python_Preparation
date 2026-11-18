# Lesson : 1.1
# Arithmetic Operators
# 1.Addition -- Addition combines two numerical values
        # eg : basic_salary = 30000
        # bonus = 5000
        # total_salary = basic_salary + bonus
        # print("Total Salary:", total_salary)
# Total Salary: 35000 -- output

# 2.Subtraction (-) -- Subtraction calculates the difference between two numbers.
        # eg: total_leaves = 24
        # used_leaves = 8
        # remaining_leaves = total_leaves - used_leaves
        # print("Remaining Leaves:", remaining_leaves)
# Remaining Leaves: 16 -- output

# 3.Multiplication (*) -- Multiplication calculates the product of two values.
        # eg : monthly_salary = 30000
        # annual_salary = monthly_salary * 12
        # print("Annual Salary:", annual_salary)
# Annual Salary: 360000 -- output
# You can also use multiplication with strings.
# print("Python " * 3)
# Output:
# Python Python Python -- This repeats the string three times.

# 4.Division (/) -- Division calculates how many times one number can be divided by another.
        # eg: annual_salary = 360000
        # monthly_salary = annual_salary / 12
        # print("Monthly Salary:", monthly_salary)
# Monthly Salary: 30000.0 -- output 
# Even though both inputs are integers, / returns a float in Python.
# Important: Division by zero is not allowed.
# print(10 / 0)
# This raises:ZeroDivisionError

# 5.Floor division (//) -- Floor division divides two numbers and rounds the result down to the nearest integer value mathematically.
        # eg : a = 20
        # b = 3
        # result = a // b
        # print(result)
# 20 / 3 = 6.666... -- its give 6 simply round off the output into nearest integer.

# 6.Modulus (%) -- The modulus operator returns the remainder after division.
        # eg : a = 20
        # b = 3
        # result = a % b
        # print(result)
# Output is 2 
# eg:   # number = input("Enter a number:")
        # number = int(number)
        # if(number %2 ==0):
        # print("The value is Even")
        # else:
        # print("The value is Odd")
# 7.Exponentiation (**) -- Exponentiation calculates the power of a number.
# EG 1 :
        # a = 2
        # b = 3
        # result = a ** b
        # print(result)
# Eg 2 :
#      principle = 10000
#      rate = 0.05
#      years = 2
#      amount = principle * (1+rate) ** years
#      print(amount)
# output : 11025.0
# Understanding calculation order (operator precedence) -- What happens when an expression contains multiple operators?
# eg 1 : 
        # result = 10 + 5 * 2
        # print(result)
# eg 2 :
# highest precedence to lowest precedence -- (),**,*,/,//,%,+,-


# Practical exercise — Employee Salary Calculator

# number_of_employees = 4
# employee_salary = 30000
# expenses = 12000

# annual_salary = employee_salary * 12 
# bonus = employee_salary + 5000
# remaining_salary = employee_salary - 12000

# print("Employee Salary Calculator")
# print(f"Employees:",number_of_employees)
# print(f"Salary:",employee_salary)
# print(f"Annual Salary:",annual_salary)
# print(f"Salary_after_bonus:",bonus)
# print(f"Remaining_Salary:",remaining_salary)
