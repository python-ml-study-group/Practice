import pandas as pd
df=pd.read_csv('newdf.csv',parse_dates=['day'])

df.set_index('day',inplace=True)
print(df)
newdf1=df.fillna({'temperature':0,'windspeed':0,'event':'No Event'

})
print(newdf1)