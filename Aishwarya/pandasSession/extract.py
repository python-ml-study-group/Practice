import pandas as pd
df=pd.read_csv('employees.csv')
first_letter=df['FIRST_NAME'].str[0]
last_letter=df['FIRST_NAME'].str[-1]
first_three_letters=df['LAST_NAME'].str[:3]
df['SPECIAL_CODE']=first_letter+last_letter+first_three_letters
print(df)
print(df['SPECIAL_CODE'])
