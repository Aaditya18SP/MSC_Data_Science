import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

#Step 1: Load the Titanic Dataset
titanic = sns.load_dataset('titanic')

#Step 2: Inspect the Dataset
print("First 5 rows of the Titanic dataset:")
print(titanic.head())

#Step3: Check for missing values
print("\nMissing values in each column:")
print(titanic.isnull().sum())

#Check data types
print("\nData types and basic statistics:")
print(titanic.info())

#Check stastical summary
print("\n statistical Summary:")
print(titanic.describe())

#Check shape of dataset
print("\n Shape of dataset:")
print(titanic.shape)

#Step 3: Handle Missing Values
#Fill missing 'age' values with the median of the 'age' column
titanic['age'].fillna(titanic['age'].median(), inplace=True)

#Fill missing 'embarked' values with the most common value (mode)
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

#Drop 'deck' column due to a large number of missing values
titanic.drop(columns=['deck'], inplace=True)

#Fill missing 'embark_town' with the mode
titanic['embark_town'].fillna(titanic['embark_town'].mode()[0], inplace=True)

#Drop any remaining rows with missing values
titanic.dropna(inplace=True)
print("\nMissing values after cleaning:")
print(titanic.isnull().sum())
