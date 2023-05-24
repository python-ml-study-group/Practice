employees = [
    {'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
    {'name': 'Bob', 'salary': 60000, 'department': 'Sales'},
    {'name': 'Charlie', 'salary': 70000, 'department': 'Marketing'},
    {'name': 'Dave', 'salary': 80000, 'department': 'Marketing'},
    {'name': 'Evan', 'salary': 90000, 'department': 'Engineering'},
    {'name': 'Fresno', 'salary': 100000, 'department': 'Engineering'}
]


def department_salaries(employees):
    department_totals = {}

    for employee in employees:
        department = employee['department']
        salary = employee['salary']

        if department in department_totals:
            department_totals[department] += salary
        else:
            department_totals[department] = salary

    return department_totals


department_totals = department_salaries(employees)
print(department_totals)
