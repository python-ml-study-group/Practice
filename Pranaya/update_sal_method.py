#Create a method in the Employee class called update_salary() that allows updating the salary of an employee. The method should take a new salary as a parameter
#and update the salary attribute.
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary): #allows updating salary of employee
        self.salary = new_salary

employee1 = Employee("Sweety", 500000) # Create employee object
print(f"Employee: {employee1.name}, Salary: ${employee1.salary}") 

employee1.update_salary(600000) # Update the salary of the employee
print(f"Employee: {employee1.name}, Updated Salary: ${employee1.salary}") #printing updated salary 
