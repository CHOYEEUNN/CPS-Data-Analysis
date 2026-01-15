import pandas as pd

data = pd.read_csv("cps_data.csv", encoding="utf-8")
print(data.describe())