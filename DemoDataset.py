import pandas as pd
import numpy as np

data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva', 'Frank', 'Grace', 'Henry', None, 'Jack'],
    'Age': [25, 32, None, 45, 28, 33, 40, None, 52, 29],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'M', None, 'M'],
    'PurchaseAmount': [120.50, 90.25, 200.00, None, 75.60, 300.45, None, 150.75, 80.30, 220.00],
    'Membership': ['Gold', None, 'Silver', 'Bronze', 'Gold', 'Silver', None, 'Bronze', 'Silver', 'Gold'],
    'LastPurchaseDate': pd.to_datetime(['2023-01-15', '2023-02-20', None, '2023-01-05', 
                                      '2023-03-10', None, '2023-02-28', '2023-03-15', 
                                      '2023-01-22', '2023-03-01'])
}

df = pd.DataFrame(data)
df_c = df[df["Membership"].notna()]
df_c["Age"].fillna(df["Age"].mean(),inplace=True)
df_c = df_c[df_c['Name'].notna()].reset_index(drop=True)
df_c = df_c.drop("LastPurchaseDate",axis=1)
print(df,"\n")
print(df_c)
