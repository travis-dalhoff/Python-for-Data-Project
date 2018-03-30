import sqlite3
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 10, 5

#Creates and Connects to the database
con = sqlite3.connect("C:\\Users\\Travis\\Desktop\\python_final_project\\cereal_data_db.db")

#Fetches data from the .csv and loads it into DataFrame
df = pd.read_csv("C:\\Users\\Travis\\Desktop\\python_final_project\\cereal.csv")

#Loads the data fetched from the .csv and loads it into the sqlite table in db, adds data if table already exists
cereal_data = df.to_sql("cereal_data", con, if_exists = "replace", index = False)


df1 = pd.read_sql_query("SELECT sugars, rating FROM cereal_data ORDER BY sugars ASC", con)

#Use matplotlib to create the chart
plt.plot(df1['sugars'], df1['rating'], 'bo')

plt.title("Sugars vs Ratings")
plt.ylabel("Ratings")
plt.xlabel("Sugars")
plt.show()


