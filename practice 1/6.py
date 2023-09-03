import pandas as pd
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)

pd.concat([data['data'], data['target']], axis=1)

print(data['data'].info())
print()
print(data['data'].isna().sum())
print()
print(data['data'].loc[(data['data']['HouseAge'] > 50) & (data['data']['Population'] > 2500)])
print()
print(data['target'].max())
print()
print(data['target'].min())
print()
print(data['data'].apply(pd.DataFrame.mean))
