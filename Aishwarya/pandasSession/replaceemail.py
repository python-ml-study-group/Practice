import pandas as pd
import re
df=pd.read_csv('employees.csv')
def replaceSpecial(email):
     email = re.sub(r'[^a-zA-Z0-9@._-]', '', email)
     email=email.lower()
     return email

df['EMAIL']=df['EMAIL'].apply(replaceSpecial)
print(df)
