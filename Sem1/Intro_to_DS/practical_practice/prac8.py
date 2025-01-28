import pandas as pd

#creating dataframe
df1= pd.DataFrame({"age":[23, 34,22], "bg":["AB+", "A+", "B+"]}, index=["A", "B", "C"])
print(df1.head())

df2 = pd.DataFrame([[23,"AB+"],[43, "A+"],[35,"B+"]], index=["A", "B", "C"], columns=["age","blood_group"])
print(df2.head())

df3 = pd.read_csv("../Practicals/Practical_7_Data_Wrangling/youtube.csv")
print(df3.head())

# READING /ACCESSING data from dataframe
#indexing
print()

#access rows using index numbers
print(df3[2:])

#access rows using column names.
#Remember=> It uses the bracket operator as the key to the dictionary. And dataframe is just a dictionary of series with column names as keys
print(df3["Ch_name"])

print()
print("boolean indexing")

print(df3[df3["Ch_name"].str.contains("T-")])

print()
print()

print("#1. using loc to access the index and columns")

# use the slicing operator
print(df3.loc[2: ,"Ch_name":])
print()

#select the row
print(df3.loc[44])
print()

#select a column
print(df3.loc[:, "Ch_name"])
print()

#one specific element
print(df3.loc[44,"Ch_name"])
print()

#iloc is deprecated, prefer using loc instead of iloc 
print("iloc: ", df3.iloc[2,3])

print()
print()
print()

# UPDATING DATA from dataframe

#1. Type casting

#2. string manipulations
print(df3["Uploads"].dtype)

# looping over each element using map
df3["Uploads"] = df3["Uploads"].map(lambda x: "".join(str(x).split(",")))

print(df3.isna())
# Type casting
df3=df3.astype({"Uploads": "float32"})
print(df3.head())
print(df3.dtypes)

def rankMapper(ele):
    if "th" in ele :
        return ele.removesuffix("th")
    elif "nd" in ele :
        return ele.removesuffix("nd")
    elif "rd" in ele:
        return ele.removesuffix("rd")
    elif "st" in ele:
        return ele.removesuffix("st")
    else:
        return ele

df3["Rank"] = df3["Rank"].map(rankMapper)

df3 = df3.astype({"Rank":"int"})
print(df3.head())


def subMapper(ele):
    if "K" in ele:
        return float(ele.removesuffix("K"))*1000
    elif "M" in ele:
        return float(ele.removesuffix("M"))*1000000
    else:
        return float(ele)

df3["Subscriptions"] = df3["Subscriptions"].map(subMapper).astype('float')


df3["Views"] = df3["Views"].map(lambda x: "".join(x.split(","))).replace("--",0).astype('int64')
print(df3.dtypes)

#3. Columns

#either insert it as a dictionary

print()
print()
#using df.assign() to construct it using an existing column

df3 = df3.assign(temp_new = df3["Rank"]+df3["Subscriptions"])
print(df3.head())


#4. Rows
#adding a new row
print()
print()
new_row = {"age": 21, "bg": "o+"}
temp_df = pd.DataFrame(new_row, index=["NEW"])
df1 = pd.concat([df1,temp_df])
print(df1.head())

print()
print()
print()

# DELETING DATA from dataframe
df3 = df3.drop(columns=["Rank"], index =[x for x in range(2,45)])
print(df3.head())

print()
print()
df3 = df3.drop_duplicates()
print(df3.nunique())
print()
print(df3.tail())

#Handling missing values

#1. detecting missing values using .isna()

#. fillna(value)
print()
print()
df3 = df3.fillna(df3.mean())
print(df3.tail())
print()
# dropna = drops entire rows or columns
#by default drops the rows
df3.dropna(axis =0)

