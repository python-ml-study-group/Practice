employees= [{'name': 'Alice', 'salary': 50000, 'department': 'sales'},
    {'name': 'Bob', 'salary': 60000, 'department': 'sales'},
   {'name': 'c', 'salary': 60000, 'department': 'engineering'},
   {'name': 'A', 'salary': 60000, 'department': 'marketing'},
   {'name': 'D', 'salary': 50000, 'department': 'marketing'}]

tot_sal={}
for emp in employees:             #looping through each dict of employees
    dept=emp['department']        #stores the value of the department key 
    sal=emp['salary']             #stores the value of the department key 

    if dept not in tot_sal:       #checks if current dept is in tot_sal dict
        tot_sal[dept]=0            

    tot_sal[dept]+=sal            #stores the sum of total salary of common dept 

print(tot_sal)