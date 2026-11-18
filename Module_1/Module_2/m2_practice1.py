# Lesson : 2.2 -- Comparison Operators
# Comparison operators are used to compare two values -- Python evaluates the comparison and returns a Boolean result:
# 1. == -- Equal to (Checks whether two values are equal.)
    # employee_age = 25
    # print(employee_age == 25) -- True
    # print(employee_age == 30) -- False
# 2.Not equal to (!=) -- Checks whether two values are different.
    # employee_department = "IT"
    # print(employee_department != "HR") -- True
    # print(employee_department != "IT") -- False
# 3.Greater than (>) -- Checks whether the left value is greater than the right value.
    # employee_salary = 35000
    # print(employee_salary > 30000) -- True
    # print(employee_salary > 50000) -- False
# 4.Less than (<) -- Checks whether the left value is smaller than the right value.
    # employee_age = 21
    # print(employee_age < 25) -- True
    # print(employee_age < 18) -- False
# 5.Greater than or equal to (>=) -- Checks whether the left value is greater than or equal to the right value.
    # employee_age = 18
    # print(employee_age >= 18) -- True
# 6.Less than or equal to (<=) -- Checks whether the left value is smaller than or equal to the right value.
# employee_age = 18
    # print(employee_age <= 18) -- True
    # print(employee_age <= 25) -- True

    # employee_age = 21
    # minimum_age = 18
    # is_eligible = employee_age >= minimum_age
    # print("Employee Age:", employee_age)
    # print("Minimum Age:", minimum_age)
    # print("Eligible:", is_eligible)

# 7. Your practical exercise

# employee_age = 24
# minimum_age = 18
# employee_salary = 35000
# required_salary = 30000

# print("Exactly 24 years old:", employee_age == 24)
# print("Younger than 18:", employee_age < 18)
# print("Age eligible:", employee_age >= minimum_age)
# print("Salary greater:", employee_salary > required_salary)
# print("Salary different:", employee_salary != 30000)
# print("Age <= 24:", employee_age <= 24)


# experience = 3
# expected_salary = 40000
# department = "IT"

# can_apply = (
#     experience >= 2
#     and expected_salary < 50000
#     and (department == "IT" or department == "HR")
# )

# print("Can Apply:", can_apply)

# candidate_age = 24
# candidate_experience = 3
# expected_salary = 40000
# candidate_department = "IT"

# # 1. Age and experience eligibility
# age_experience_eligible = (
#     candidate_age >= 18
#     and candidate_experience >= 2
# )

# # 2. Department eligibility
# department_eligible = (
#     candidate_department == "IT"
#     or candidate_department == "HR"
# )

# # 3. Salary eligibility
# salary_eligible = expected_salary < 50000

# # 4. Check whether the candidate is NOT from Finance
# not_finance = candidate_department != "Finance"

# # 5. Overall job eligibility
# job_eligibility = (
#     candidate_age >= 18
#     and candidate_experience >= 2
#     and (candidate_department == "IT" or candidate_department == "HR")
# )

# # Display results
# print("========== JOB ELIGIBILITY CHECKER ==========")
# print("Age and Experience Eligible:", age_experience_eligible)
# print("Department Eligible:", department_eligible)
# print("Salary Eligible:", salary_eligible)
# print("Not from Finance:", not_finance)
# print("Overall Job Eligibility:", job_eligibility)

# Practical exercise — Employee Salary Updater

# employee_salary = 30000
# print("Original Salary:", employee_salary)
# employee_salary += 2000
# print("After Increment:", employee_salary)
# employee_salary -= 2000
# print("After Deduction:", employee_salary)
# employee_salary *= 2
# print("After Multiplication:", employee_salary)
# employee_salary /= 2
# print("After Division:", employee_salary)

# Lesson : 2.5 -- Conditional Statements (if, elif, else)

# performance_score = input("Enter the Score:")
# performance_score =int(performance_score)

# if performance_score >= 90:
#     print("Excellent")
# elif performance_score >= 75:
#     print("Good")
# elif performance_score >= 50:
#     print("Average")
# else:
#     print("Needs Improvement")

# Lesson : 2.6 -- Nested Condition

# username = "mithu"
# password = "python123"

# if username == "mithu":
#     print("Username found.")

#     if password == "python123":
#         print("Login successful.")
#     else:
#         print("Incorrect password.")

# else:
#     print("Username not found.")

# employee_name = "Mithu"
# employee_experience = input("Enter employee experience:")
# performance_score = input("Enter performance score:")

# employee_experience =int(employee_experience)
# performance_score = int(performance_score)

# if employee_experience >= 3:
#     print("Experience is sufficient")

#     if performance_score >= 80:
#         print("Eligible for promotion")

#     else :
#         print("Performance score is insufficient")

# else:
#     print("Insufficient Experience")

# IF Experience >= 3
#     |
#     TRUE
#     |
#     Check Performance >= 80
#        |
#        TRUE  → Eligible for promotion
#        FALSE → Performance insufficient

#     FALSE → Insufficient experience

# Ternary Expression 

# Syntax -- > variable = value_if_true if condition else value_if_false
# eg -- > result = "Eligible" if age >= 18 else "Not Eligible"
# eg 2: 
    # num = 7 
    # result = "Even" if num % 2== 0 else "Odd"
    # print (result)
# When Should You Use Ternary Expressions?
# Use them when:
# - You have a simple if-else condition.
# - You only need to choose between two values.
# - The expression remains easy to read.
# For example, don't force complicated logic into one line. Normal if-elif-else is better for that.

# Employee Attendance Status Checker.
# emp_name = "Mithu"
# attendence_per = 85

# exam_status = "ElIgible for exam" if attendence_per >= 75 else "Not Eligible for Exam"
# print(f"Employee: {emp_name}")
# print(f"Attendance: {attendence_per}%")
# print(f"Exam Status: {exam_status}")

# project: Eligibility Checker


# candidate_age = input("Enter your age: ")
# required_age = 18

# candidate_age = int(candidate_age)

# if candidate_age >= required_age:
#     result = "You are eligible"
# else:
#     result = "You are not eligible"

# print("ELIGIBILITY CHECKER")
# print("-------------------")
# print(f"Candidate Age: {candidate_age}")
# print(result)
# print(f"Minimum required age: {required_age}")
