class employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  def update_salary(self, new_salary):
    self.salary = new_salary
employee = employee('nagasai', 30000)
print(employee.salary)
employee.update_salary(50000)
print(employee.salary)
