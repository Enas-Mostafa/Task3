import pandas as pd
df1=pd.read_csv("Customers.csv")
print('Before removing:',df1.shape)
df2=df1.dropna()
print('After removing:',df2.shape)
print("--------------------------")
print("Number of null rows =",df1.shape[0]-df2.shape[0])
print("--------------------------")
