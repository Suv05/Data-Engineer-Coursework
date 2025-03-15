import sqlite3
import pandas as pd

conn = sqlite3.connect("./SQLite3/MANAGER.db")  # conn made

table_name = "MANAGER"
attribute_list = ["DEPT ID", "DEP NAME", "MANAGER ID", "LOC ID"]  # headers assign

file_path = "./SQLite3/Departments.csv"
df = pd.read_csv(file_path, names=attribute_list)  # create dataframe

df.to_sql(table_name, conn, if_exists="replace", index=False)  # load to db
print("Table created successfully")

# append some data
data_dict = {
    "DEPT ID": [9],
    "DEP NAME": ["Quality Assurance"],
    "MANAGER ID": ["30010"],
    "LOC ID": ["L0010"],
}
df = pd.DataFrame(data_dict)
df.to_sql(table_name, conn, if_exists="append", index=False)

# querying
# for viewing all data
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# total no of rows
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# only department name
query_statement = f"SELECT `DEP NAME` FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()
