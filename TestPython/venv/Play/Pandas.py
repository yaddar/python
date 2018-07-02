import pandas
from datetime import datetime

print(datetime.now())

df1 = pandas.read_csv("C:/Users/yarona/Downloads/supermarkets.csv")
print(df1.mean());


# df2 = pandas.read_excel("C:/Users/yarona/Downloads/supermarkets.xlsx")