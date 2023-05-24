"""For the provided example, create 
a new class “Director”, whose 
bonus calculation is same as 
manager"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1 # # Calculate bonus as 10% of the salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # Call the parent class's __init__ method to set name and salary
        self.department = department 

    def calculate_bonus(self):
        return self.salary * 0.15 # Calculate bonus as 15% of the salary for managers


class Director(Manager):  # Inherits from Manager instead of Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)  # Call Manager's __init__ method

employee1 = Employee("John", 50000)
manager1 = Manager("Andrew", 80000, "Sales")
director1 = Director("Dale", 100000, "Operations")

# Print details and bonuses
print(f"Employee: {employee1.name}, Bonus: ${employee1.calculate_bonus()}")
print(f"Manager: {manager1.name}, Department: {manager1.department}, Bonus: ${manager1.calculate_bonus()}")
print(f"Director: {director1.name}, Department: {director1.department}, Bonus: ${director1.calculate_bonus()}")

