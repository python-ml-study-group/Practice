import pandas as pd
# Read the CSV file in to a dataframe
df = pd.read_csv('employees.csv')
df['FIRST_NAME']=df['FIRST_NAME'].str.replace('D','')

# Remove leading and trailing white spaces from 'first name' column
df['FIRST_NAME'] = df['FIRST_NAME'].str.strip()

# Remove leading and trailing white spaces from 'last name' column
df['LAST_NAME'] = df['LAST_NAME'].str.strip()

# Print the updated DataFrame
print(df['FIRST_NAME'],df['LAST_NAME'])

