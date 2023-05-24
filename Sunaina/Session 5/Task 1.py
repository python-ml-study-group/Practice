""" Create a method in the Employee 
class called update_salary() that 
allows updating the salary of an 
employee. The method should 
take a new salary as a parameter 
and update the salary attribute. """

class Employee:
    def __init__(self, name, salary): # initializes the name and salary attributes of an employee object
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary): # updating the salary of the employee object
        self.salary = new_salary

employee1 = Employee("Jack", 50000) # Create an instance of the Employee class with name and salary
print(f"Employee: {employee1.name}, Salary: ${employee1.salary}") # Print the name and salary of the employee

employee1.update_salary(60000) # Update the salary of the employee
print(f"Employee: {employee1.name}, Updated Salary: ${employee1.salary}") # Print the name and updated salary of the employee
