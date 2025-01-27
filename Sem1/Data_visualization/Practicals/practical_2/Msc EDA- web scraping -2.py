#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install requests


# In[5]:


pip install html5lib


# In[6]:


pip install bs4


# In[12]:


import webbrowser
dir(webbrowser)
webbrowser.open('wwww.python.org')


# In[9]:


import webbrowser
webbrowser.open_new('https://www.python.org')


# In[14]:


import webbrowser
webbrowser.open_new_tab('https://www.python.org')


# In[13]:


import webbrowser
dir(webbrowser)


# In[17]:


import webbrowser
c = webbrowser.get('safari')
c.open('https://www.python.org')
c.open_new_tab('https://www.python.org')


# In[12]:


import requests
URL = "https://www.python.org/blogs/"
response = requests.get(URL)

print(type(response))

print(response.text[:300])


# In[2]:


import bs4
dir(bs4)


# In[13]:


import requests
URL = "https://www.python.org/blogs/"
response = requests.get(URL)
print(requests.codes.processing)
print(requests.codes.ok)
print(requests.codes.not_found)


# In[15]:


import requests
response = requests.get('https://www.python.org')
if response.status_code == requests.codes.ok :
    print(len(response.text))
    print(response. text[:251])


# In[20]:


import requests
res = requests.get('http://amazon.in/applyIjobs.html')
try:
    res.raise_for_status()
except Exception as exc:
    print( 'There was a problem: %s'% (exc))


# In[17]:


import os
import requests
res = requests.get('https://www.python.org')

try:
    res.raise_for_status()
    file_path = os.path.join(directory, 'ds.html')
    trainingFile = open('ds.html','wb')
    print("file saved scuccessfully")
    for chunk in res.iter_content(1000):
        trainingFile.write(chunk)
        trainingFile.close
except Exception as exc:
                       print ('There was a problem: %s'%(exc))


# In[5]:


import requests
# URL of the page to fetch
url = 'https://www.python.org/blogs/'
try:
    res = requests.get (url)

    res.raise_for_status()

    file_path = r'ds2.html'
    
    with open(file_path,'wb') as trainingFile:
        for chunk in res.iter_content(1000):
            trainingFile.write(chunk)
    print("file saved succesfully")
    
except Exception as exc:
    print("error : %s"%(exc))


            


# In[18]:


import requests,bs4

res = requests.get( 'https://www.python.org/blogs/')
try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    links = soup.find_all('a')
    for link in links:
        print(link)
except Exception as exc:
    print( 'There was a problem: %s' % (exc))


# In[20]:


import requests
from bs4 import BeautifulSoup
URL = "https://www.python.org/blogs/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify())


# In[25]:


print(soup.title)


# In[26]:


print (soup.find_all("img"))


# In[28]:


print (soup.get_text())


# In[29]:


print (soup.head)


# In[30]:


pip install builtwith


# In[47]:


import builtwith
url = "https://www.python.org"
print(builtwith.parse(url))


# In[41]:


import builtwith
dir(builtwith)


# In[48]:


import builtwith
builtwith.builtwith('http://wordpress.com')


# In[37]:


pip install python-whois


# In[39]:


import whois
print(whois.whois('python.org'))


# In[55]:


import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
res = requests.get(url)

if response.status_code == 200 :
    soup = BeautifulSoup(response.text,"html.parser")
    
    quotes_data = []
    
    quotes= soup.findAll('span', class_='text')
    authors = soup.findAll('small', class_='author')
    
    
    for i in range(len(quotes)):
        quote_text= qoutes[i].text
        author = authors[i].text
        quotes_data.append({'quote': quote_text, ' author' : author})
        
        
        for entry in quotes_data:
            print(f"Quote : {entry['quote']}")
            print(f"Author: {entry['author']}")
            print("-----")
            
    else:
        print("error")


# In[56]:


import requests
from bs4 import BeautifulSoup
 
# Step 1: Send an HTTP request to the website
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
 
# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
 
    # Step 3: Find all the quotes and authors
    quotes_data = []  # To store the quotes and authors
 
    # In the website, quotes are inside <span> tags with class 'text' and authors in <small> tags with class 'author'
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
 
    # Step 4: Loop through the quotes and authors, and store them in a dictionary
    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author = authors[i].text
        quotes_data.append({'quote': quote_text, 'author': author})
 
    # Step 5: Display the scraped data
    for entry in quotes_data:
        print(f"Quote: {entry['quote']}")
        print(f"Author: {entry['author']}")
        print('---')
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
 


# In[60]:


# 2nd practical 

import requests

API_KEY ="ee532018a5d03edd77ec27c9088064d4"

city = "Mira-Bhayander"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
 
# Send a GET request to the API
response = requests.get(url)
 
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Reason: {response.reason}")


# In[26]:


import mysql.connector
def connect_to_database(host, user, password, database):
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     cursorclass=pymysql.cursors.DictCursor)
        print("Connected to the database successfully!")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
host = 'Shridayals-MacBook-Air.local'
user = 'root'
password = 'data@1234'
database = 'azad'



# In[32]:


# sunday 22 sep 
import mysql.connector

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(
        host="Shridayals-MacBook-Air.local",  # Add a comma here
        user="root",  # Add a comma here
        password="data@1234",  # Add a comma here
        database="azad"  # Corrected the format
    )

    if connection.is_connected():
        print("Successfully connected to the database")

        # Create a cursor object
        cursor = connection.cursor()

        # Define your SQL query
        query = "SELECT * FROM Admin"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the result
        results = cursor.fetchall()

        # Write the results to a file
        with open("output.txt", "w") as file:
            file.write("ID\tName\tEmail\n")  # Header for the file
            file.write("----------------------------\n")
            for row in results:
                file.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")

        print("Data successfully written to 'output.txt'")

    else:
        print("Failed to connect to the database")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# In[9]:


#23 monday practical 3rd , data cleaning and processing 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the Titanic dataset
t = sns.load_dataset("titanic")

# Display the first few rows of the dataset
print(t.head())


# In[10]:


print(t.isnull().sum())


# In[12]:


print(t.info())
t.describe()


# In[14]:


print(t.shape)


# In[16]:


t['age'].fillna(t['age'].median(), inplace = True)


# In[17]:


t['embarked'].fillna(t['embarked'].mode(), inplace = True)


# In[18]:


t.drop(columns=['deck'],inplace = True )


# In[19]:


t['embark_town'].fillna(t["embark_town"].mode()[0],inplace = True)


# In[22]:


t.dropna(inplace=True)


# In[23]:


t.isnull().sum()


# In[26]:


t.describe()


# In[27]:


print(t.shape)


# In[34]:


lable_encoder = LabelEncoder()
t['sex']= lable_encoder.fit_transform(t['sex'])
t['embarked']= lable_encoder.fit_transform(t['embarked'])
t['who'] = t['who'].apply(lambda x: 1 if x == 'man' else 0)


# In[ ]:


t['family_size'] = t['sibsp'] + t['parch'] +1


# In[35]:


tc = t.drop_duplicates()


# In[40]:


plt.figure(figsize=(5,4))
plt.boxplot(tc['fare'])
plt.title("Box plot for Fare (outliers detection)")
plt.show()


# In[41]:


fare_cap = tc['fare'].quantile(0.99)
tc['fare'] = np.where(tc['fare'] > fare_cap, fare_cap, tc['fare'])
print(tc['fare'].describe())


# In[42]:


s = StandardScaler()
tc[['age', 'fare']] = s.fit_transform(tc[['age', 'fare']])


# In[45]:


tc.describe()
print(tc.head())


# In[46]:


tc.to_csv('tc.csv', index=False)
print("\nCleaned dataset saved to 'tc.csv")


# In[3]:


#HW given at 23 sep monday

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load the California Housing Dataset
housing = fetch_california_housing()
hdf = pd.DataFrame(housing.data, columns=housing.feature_names)

# Step 2: Inspect the Data
print("First 5 rows of the California Housing dataset:")
print(hdf.head())


# In[7]:


hdf.isnull()


# In[ ]:




