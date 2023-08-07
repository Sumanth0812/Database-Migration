import numpy as np
import pandas as pd
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="0812",database="test1")

cur=conn.cursor()

query="select *from school"

data = pd.read_sql(query, conn)

data['parents_number'] = data['parents_number'] + 10

print(data)

data.to_csv('transformed_data.csv', index=False)

import os
print(os.getcwd())



