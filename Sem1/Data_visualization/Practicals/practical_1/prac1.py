import pandas as pd
from sqlalchemy import create_engine

dataset={
        "name": ["ABC","DEF","GHI","JKL"],
        "age":[18,32,65,7],
        "blood_group":["A+","B+","O+","AB+"]
        }

df= pd.DataFrame(dataset)
print(df["name"].dtype)
print(df["age"].dtype)
print(df["blood_group"].dtype)
write=False
'''
////////////////////////
Storing Data
/////////////////////////
'''

if(write):
    #to csv
    df.to_csv('data.csv')

    #to json
    df.to_json('data.json')

    #to html
    df.to_html('data.html')

    #to xml
    df.to_xml('data.xml')

    #text format
    string = df.to_string()
    with open("data.txt","w") as file:
        file.write(string)

    #Spreadsheet formats
    #to excel
    df.to_excel('data.xlsx')

    #Database format
    #to sql
    engine= create_engine("mysql+mysqlconnector://root@localhost/dv")
    df.to_sql('people',engine)

    #Binary format
    #to pickle
    df.to_pickle('data.pkl')



'''
////////////////////////
Reading Data
/////////////////////////
'''

#Text data
d_csv = pd.read_csv("data.csv")
print("\n=====CSV file=====")
print(d_csv)

d_json = pd.read_json("data.json")
print("\n=====JSON file=====")
print(d_json)

d_html = pd.read_html("data.html")
print("\n=====HTML file=====")
print(d_html)

d_xml = pd.read_xml("data.xml")
print("\n=====XML file=====")
print(d_xml)

d_text = pd.read_table("data.txt")
print("\n=====Text file=====")
print(d_text)

#excel data
d_excel = pd.read_excel("data.xlsx")
print("\n=====EXCEL output=====")
print(d_excel)

#sql data
engine= create_engine("mysql+mysqlconnector://root@localhost/dv")
d_sql = pd.read_sql("people", engine)
d_sql2= pd.read_sql("Select * from users;", engine)
print("\n=====SQL=====")
print("====People table output===")
print(d_sql)

print()
print("====Users table output===")
print(d_sql2)

#binary
d_pickle = pd.read_pickle("data.pkl")
print("\n=====Pickle file=====")
print(d_pickle)
