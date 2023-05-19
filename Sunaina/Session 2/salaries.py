""" You're given a list of dictionaries containing information about
different employees in a company. Each dictionary has keys for the
employee's name, salary, and department. Your task is to write a Python
function that returns a dictionary containing the total salary for each
department.
employees = [{'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
{'name': 'Bob', 'salary': 60000, 'department': 'Sales'}} Output: {'Sales': 110000, 'Marketing': 150000, 'Engineering': 190000}
"""

employees = [
    {'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
    {'name': 'Bob', 'salary': 60000, 'department': 'Sales'},
    {'name': 'Charlie', 'salary': 70000, 'department': 'Marketing'},
    {'name': 'David', 'salary': 80000, 'department': 'Marketing'},
    {'name': 'Eve', 'salary': 90000, 'department': 'Engineering'},
    {'name': 'Frank', 'salary': 100000, 'department': 'Engineering'}
]

# Define a function to calculate the total salary for each department

def department_salaries(employees):
    department_totals = {}
    for employee in employees:
        
        # Check if the department is already in the dictionary
        if employee['department'] not in department_totals:
            
            # If not, add the department with the current salary
            department_totals[employee['department']] = employee['salary']
        else:
            
            # If yes, add the current salary to the existing department
            department_totals[employee['department']] += employee['salary']
    return department_totals

# Call the function with the given list of employees and assign the returned dictionary to department_totals
department_totals = department_salaries(employees)

# Print the dictionary containing the total salary for each department
print(department_totals)
