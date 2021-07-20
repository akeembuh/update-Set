import pandas as pd
df = pd.read_csv("python hands-on - dataset.csv")
df

#View data type
df.dtypes

# make the "date" cloumn in to date and time or int value with pandas 
df['date'] = pd.to_datetime(df.date)
df

#now view the data type again to verify if "date" column
df.dtypes

df['Year'] = df.date.dt.year #This line is not important but for clearity. It can also be commented out as it does not affect or add anything value to the data
df

year_stamp = df['Year'].loc[(df.Year < 2021) & (df.Year >= 2021)] #comparing the year in bool
year_stamp = df.Year < 2021 # putting the bool in "year_stamp" to give us "True" or "False" value

df.to_json(r'updated_dataset.json') #save to json format.
