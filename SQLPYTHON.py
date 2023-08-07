import pandas as pd
import numpy as np
import pyodbc as odbc

# Connection details
server = 'Laptop-Qk3BK7PL'
database = 'test1'
username = 'root'
password = '0812'

# Establish the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# SQL query to retrieve data from a table
sql_query = "SELECT * FROM School"

# Execute the query and fetch the data into a pandas DataFrame
data = pd.read_sql(sql_query, conn)

# Close the database connection
conn.close()

# Print the retrieved data
print(data)
