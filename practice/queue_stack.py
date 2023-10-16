# Implement the undo feature using stack (deque)
from collections import deque

# Create a stack
changes = []

changes.append("Type (abc)")
changes.append("Color (red)")
changes.append("Underline (small)")

changes.insert(0, "Inserted @ 0")
print (changes)


t1 = ("Roopesh", 40, "PhD", "Bangalore")

# create the namedtuple
from collections import namedtuple
Employee = namedtuple('Employee', 'name age qualification city')
e1 = Employee(name="Roopesh", age=40, qualification="PhD", city="Bangalore")
print (e1.city)
print (t1 [2])