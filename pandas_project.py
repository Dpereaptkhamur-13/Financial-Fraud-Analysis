#Project: Capstone project of financial data using python
#loading -> cleaning -> transformation -> aggregation -> visualization

#Step 1 : import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 2 : Load the data
df = pd.read_csv("Synthetic_Financial_datasets_log.csv")
print(df.head()) #output 5 rows from data
print(df.info()) #check metadata

#Step 3 : Data Cleaning
#handle missing value, correct data types, remove duplicates
print(df.isnull().sum())
df.drop_duplicates(inplace=True) #remove duplicates

#Step 4 : transformation
#feature engineering - new column addition
#categorization - group of numeric data for better analysis
df['Amount_Category'] = pd.cut(df['amount'], bins = [0, 5000, 10000, 20000], labels=["Low", "Medium", "High"])
print(df.head())

#Step 5 : Data aggregation - groupby or pivot using pandas
transaction_summary = df.groupby("type").agg(
    total_amount = ("amount", "sum"),
    avg_amount = ("amount", "mean"),
    count_trans = ("amount", "count")
).reset_index()
print(transaction_summary)

#SMA and EMA
df = df.sort_values('step')
df['SMA_20'] = df['amount'].rolling(window = 20).mean()
print(df[['amount', 'SMA_20']].iloc[20:30])

#Step 6 : Visualization - bar plot, histogram, scatter plot
plt.figure(figsize=(10, 6))
sns.barplot(x = "type", y = "total_amount", data = transaction_summary)
plt.title("Banks Data for amount groups")
plt.show()