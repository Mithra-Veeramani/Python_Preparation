# Module 3 : Loops
# for loop -- Used when you want to iterate over a sequence or a known collection of items.
# while loop -- Used when you want to repeat instructions as long as a condition remains True.

# for Loop -- practical exercise
# eg:
    # students = ["Rahul","Priya","Ananya","Vinoth"]

    # for student in students:
    #     print(student)
    #     print("Student registered successfully")

# While Loop -- Practice exercise
# eg:
    # count = 1
    # while count <= 10:
    #     print(count)
    #     count += 1

# range () -- range() generates a sequence of numbers. It is commonly used with for loops when you want to repeat something a specific number of times.
# range (start,stop) 
    # for number in range(1, 6):
    #     print(number) -- o/p: 1,2,3,4,5
# range(start, stop, step)
    # for number in range(2, 11, 2):
    #     print(number) -- o/p: 2,4,6,8,10
# eg:
# for num in range(2,21,2):
#     print(num)

# Loop Control Statement 
    # break — exits the loop immediately.
    # continue — skips the current iteration and moves to the next.
    # pass — does nothing; acts as a placeholder.
# break -- Example:
# for number in range(1, 6):    
#     if number == 3:        
#         break    
#     print(number)
# Output:
# 1
# 2
# Continue -- Example
# for number in range(1, 6):
#     if number == 3:
#         continue
#     print(number)
# Output:
# 1
# 2
# 4
# 5
# Pass -- Example 
# for number in range(1, 6):
#     if number == 3:
#         pass

#     print(number)
# Output:
# 1
# 2
# 3
# 4
# 5
# Example -- Overall
# employee_ids = [101,102,103,104,105]

# for employee_id in employee_ids:
#     if employee_id == 103:
#         continue
#     print(employee_id)

# Nested Loops  -- means a loop inside another loop

# for i in range(1, 4):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# Multiplication Table Generator -- Practice Exercise
print("MULTIPLICATION TABLE")
print("--------------------")
number = int(input("Enter a number: "))

for i in range(1,11):
    result = number * i
    print(f"{number} x {i} = {result}")