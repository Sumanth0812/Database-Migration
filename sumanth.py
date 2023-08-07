cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print("List of Databases:")
for db in databases:
    print(db[0])
