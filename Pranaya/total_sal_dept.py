employees = [{'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
             {'name': 'Bob', 'salary': 60000, 'department': 'Sales'},
             {'name': 'Charlie', 'salary': 70000, 'department': 'Marketing'},
             {'name': 'Dave', 'salary': 80000, 'department': 'Marketing'},
             {'name': 'Eve', 'salary': 90000, 'department': 'Engineering'},
             {'name': 'Frank', 'salary': 100000, 'department': 'Engineering'}]

def total_salary_by_department(employees):
    #initializes an empty dictionary called department_salary to hold the total salary for each department
    department_salary = {}

    #terates over each employee dictionary in the employees list, extracts the department and salary information
    for employee in employees:
        department = employee['department']
        salary = employee['salary']

        if department not in department_salary:
            department_salary[department] = 0
        
        department_salary[department] += salary

    return department_salary

employee_salaries = total_salary_by_department(employees)
print(employee_salaries)
