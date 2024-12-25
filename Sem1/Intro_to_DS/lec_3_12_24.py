import pandas as pd
import numpy as np

l1 = np.array([400,800])
l2=  np.array(["ABc", "XYZ"])

p1= pd.Series(l1)
p2=pd.Series(l2)

print(p1)
p3 = pd.Series(l1,index=p2)
print(p3)

print("\nDATA FRAME")
data_dict = {'col1': l1, 'col2':l2}
df1=pd.DataFrame(data=data_dict)
print(df1)
print()

name=np.array(["Steve","Lia","Vin","Katie"])
Age=[32,28,45,38]
Gender=["Male","Female","Male","Female"]
Rating=[3.45,4.6,3.9,2.78]

data = {"name":name, "age":Age, "gender":Gender, "rating":Rating}
df2=pd.DataFrame(data=data)
print(df2)
print()

print(df2.tail(2))
print()

print("Name indexing")
print(df2["name"])

print()
print(df2.iloc[:,0:2])
print(df2.iloc[0:2,])
print()

print(df2.loc[:,["name"]])



