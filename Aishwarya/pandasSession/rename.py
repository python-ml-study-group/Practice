import pandas as pd
df=pd.read_csv('employees.csv')
df['CONTACT_NUMBER']=df['PHONE_NUMBER']
df.drop('PHONE_NUMBER',axis=1,inplace=True)
print(df)