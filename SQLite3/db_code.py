import sqlite3
import pandas as pd

conn = sqlite3.connect("./SQLite3/STAFF.db")  # conn made

table_name = "INSTRUCTOR"
attribute_list = ["ID", "FNAME", "LNAME", "CITY", "CCODE"]  # headers assign

file_path = "./SQLite3/INSTRUCTOR.csv"
df = pd.read_csv(file_path, names=attribute_list)  # create dataframe

df.to_sql(table_name, conn, if_exists="replace", index=False)  # load to db
print("Table created successfully")

# querying
# for viewing all data
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
# print(query_statement)
# print(query_output)

# viewing only fname from data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# total no of rows
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# append some data
data_dict = {
    "ID": [100],
    "FNAME": ["John"],
    "LNAME": ["Doe"],
    "CITY": ["Paris"],
    "CCODE": ["FR"],
}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists="append", index=False)
print("Table updated successfully")

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()
