import pandas as pd

file = pd.read_csv(r"E:\test\china-city-list.csv")
file = file.loc[:, ['City_ID', 'City_CN']]
data = file.head()
print(data)
