import pandas as pd
import kagglehub
import os

#Reading DataSet
path = kagglehub.dataset_download("prevek18/ames-housing-dataset")
print("Path to dataset files:", path)
ds_path = os.path.join(path, "AmesHousing.csv")
df = pd.read_csv(ds_path)

# Show basic info
print(df.shape)
print(df.head())


#handling missing data

# print(df.isnull().sum()[df.isnull().sum() > 0])

cols = ['BsmtFin SF 1', 'Bsmt Qual','Bsmt Cond','Bsmt Exposure','BsmtFin Type 1','BsmtFin Type 2',
        'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF','Electrical', 'Bsmt Full Bath',
          'Bsmt Half Bath','Garage Cars','Garage Area']

float_cols = ['Lot Frontage','Mas Vnr Area','Garage Yr Blt','Garage Area','Garage Cars']

text_cols = ['Fireplace Qu','Pool QC','Alley','Garage Type','Garage Finish','Garage Qual','Garage Cond','Misc Feature']

df[cols] = df[cols].fillna(0)
df[float_cols] = df[float_cols].fillna(0)
df[text_cols] = df[text_cols].fillna('None')
df = df.drop(columns=['Fence','Mas Vnr Type'])

nulls = df.isnull().sum()
nulls = nulls[nulls > 0]

for col in nulls.index:
    print(f"{col}: {nulls[col]} , {df[col].dtype}")

