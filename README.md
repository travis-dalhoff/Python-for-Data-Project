# Python-for-Data-Project

Code-Louisville-Python-for-Data-Project

The final project for my Code Louisville Python for Data Course

This is the final project for my Python for Data project. With it, I want to compare cereal ratings to sugar content in the cereals. My hypothesis is cereals with higher sugar content will receive higher ratings. My data set is a CSV file from Kaggle. It contains nutritional data for 76 different cereals in addition to a rating value for each cereal. I addressed my hypothesis by creating a chart showing ratings (in descending order) on the y-axis and sugar content (in ascending order) on the x-axis. The data suggests that my hypothesis is wrong and that ratings tend to decrease as sugar content increases.

HOW TO RUN THE PROGRAM

The program works best using Jupyter Notebooks. You can copy and paste the code into a Jupyter notebook. You will need to specify in Line 11 of the code the filepath to where your database will be located. You will also need to specify in Line 14 of the code the filepath to the csv file. Please remember to use double back-slashes (\) in your filepaths to avoid encoding errors.

PROJECT REQUIREMENT CHECKLIST

README

    COMPLETE

Must include a SQL Database with Python script that sets up/creates the database.

    Line 13 creates and/or connects to the SQLite database

Must include a Python script to fetch data from a data source and load it into your SQLite database

    Line 14 fetches from the CSV file and loads it into the Pandas Data Frame
    Line 17 loads the data from the Pandas Data Frame into the SQLite database

Must inclue a Python script to retrieve the data from the SQL database into a Python object.

    Line 17 loads a SQLite table into cereal_data

Must include a Python script to modify your data so as to prepare it for visualization

    Line 20 creates a variable to that stores only the sugars and ratings columns from cereal_data table and orders the results by sugar content in ascending orders.

Visualize the results of the analysis

    Lines 22 - 27 use matplotlib to create a dot chart comparing sugar content and ratings
    Line 8 uses rcParams to resize the chart for better visualization

Project is loaded to GitHub

    Complete
