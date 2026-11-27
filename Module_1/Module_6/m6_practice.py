# # # employee_id = "EMP101"
# # # employee_name = "Rahul"
# # # employee_department = "Developer"
# # # employee_salary = 35000

# # # def display_employee_details(emp_id, emp_name, emp_dept, emp_salary):
# # #     print("Employee ID:", emp_id)
# # #     print("Employee Name:", emp_name)
# # #     print("Employee Department:", emp_dept)
# # #     print("Employee Salary:", emp_salary)

# # # display_employee_details(employee_id, employee_name, employee_department, employee_salary)

# # class Employee:
# #     pass
# # employee1 = Employee()
# # employee2 = Employee()

# # employee1.employee_id = "EMP101"
# # employee1.employee_name = "Rahul"
# # employee1.employee_department = "Developer"
# # employee1.employee_salary = 35000

# # employee2.employee_id = "EMP102"
# # employee2.employee_name = "Mohan"
# # employee2.employee_department = "Developer"
# # employee2.employee_salary = 40000

# # print("Employee 1 Details:")
# # print("Employee ID:", employee1.employee_id)
# # print("Employee Name:", employee1.employee_name)     
# # print("Employee Department:", employee1.employee_department)
# # print("Employee Salary:", employee1.employee_salary,"\n")

# # print("Employee 2 Details:")
# # print("Employee ID:", employee2.employee_id)
# # print("Employee Name:", employee2.employee_name)
# # print("Employee Department:", employee2.employee_department)
# # print("Employee Salary:", employee2.employee_salary)

# class Employee:

#     def __init__(self, emp_name, emp_id, emp_age, emp_dept, emp_salary):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_age = emp_age
#         self.emp_dept = emp_dept
#         self.emp_salary = emp_salary


# employee1 = Employee("Mithra", "EMP23", 21, "Development", 35000)
# employee2 = Employee("Anandh", "EMP22", 26, "Development", 100000)
# employee3 = Employee("Mohan", "EMP32", 26, "Testing", 50000)

# print("Employee ID:", employee1.emp_id)
# print("Employee Name:", employee1.emp_name)
# print("Employee Age:", employee1.emp_age)
# print("Employee Dept:", employee1.emp_dept)
# print("Employee Salary:", employee1.emp_salary,"\n")

# print("Employee ID:", employee2.emp_id)
# print("Employee Name:", employee2.emp_name)
# print("Employee Age:", employee2.emp_age)
# print("Employee Dept:", employee2.emp_dept)
# print("Employee Salary:", employee2.emp_salary,"\n")

# print("Employee ID:", employee3.emp_id)
# print("Employee Name:", employee3.emp_name)
# print("Employee Age:", employee3.emp_age)
# print("Employee Dept:", employee3.emp_dept)
# print("Employee Salary:", employee3.emp_salary)

class Employee:
    def __init__(self, emp_name, emp_id, emp_age, emp_dept, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_age = emp_age
        self.emp_dept = emp_dept
        self.emp_salary = emp_salary
    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Age:", self.emp_age)
        print("Employee Dept:", self.emp_dept)
        print("Employee Salary:", self.emp_salary)
    def update_employee_salary(self, new_salary):
        self.emp_salary = new_salary
        print("Employee Salary updated to:", self.emp_salary,"\n")
employee1 = Employee("Mithra", "EMP23", 21, "Development", 35000)
employee2 = Employee("Anandh", "EMP22", 26, "Development", 100000)
employee3 = Employee("Mohan", "EMP32", 26, "Testing", 50000)

employee1.display_employee()
employee1.update_employee_salary(40000)
employee2.display_employee()
employee2.update_employee_salary(120000)
employee3.display_employee()
employee3.update_employee_salary(60000)

