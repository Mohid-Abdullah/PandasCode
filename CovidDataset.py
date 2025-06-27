import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")
#data info
print(df.head)
print(df.shape)

#handling null values
print(df.isnull().sum())
df = df.drop(columns='Province/State')
df['Recovered'] = df['Recovered'].fillna(0)
print(df.isnull().sum())

#dropping duplicates
df.drop_duplicates(inplace=True)
print(df.shape)

#ready to use for a ml model