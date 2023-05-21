""" You're given a list of dictionaries containing information about
different employees in a company. Each dictionary has keys for the
employee's name, salary, and department. Your task is to write a Python
function that returns a dictionary containing the total salary for each
department.
employees = [{'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
{'name': 'Bob', 'salary': 60000, 'department': 'Sales'}} Output: {'Sales': 110000, 'Marketing': 150000, 'Engineering': 190000}
"""

#list of Dictionaries
employees = [
    {'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
    {'name': 'Bob', 'salary': 60000, 'department': 'Sales'},
    {'name': 'Siri', 'salary': 100000, 'department': 'Marketing'},
    {'name': 'Sridevi', 'salary': 80000, 'department': 'Accounting'},
    {'name': 'Satya', 'salary': 70000, 'department': 'Marketing'}
]

def salaries_of_each_department(employees):    #Function to calculate the total salary for each department
    department_totalsalary = {}                     #creates empty dictionary to get the department and its salary totals later
    for employee in employees:
        department = employee['department']     #Retrieves department for each employee
        salary = employee['salary']             #Retrieves salary for each employee

        if department in department_totalsalary:        #checks if the department is there in tha empty dictionary 
            department_totalsalary[department] += salary  #if the department is present then it adds the salary of that department
        else:
            department_totalsalary[department] = salary #if the department is not there then adds the department to the dicionary

    return department_totalsalary

# Call the function with the given list of employees and assign the returned dictionary to department_totals
department_totals = salaries_of_each_department(employees)

print(department_totals)


