import pandas as pd
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ["Name", "MC_USD_Billion"]  # upon extraction only
table_attribs_final = [
    "Name",
    "MC_USD_Billion",
    "MC_GBP_Billion",
    "MC_EUR_Billion",
    "MC_INR_Billion",
]

db_name = "./Mini-Project-2/Banks.db"
table_name = "Largest_banks"
csv_path = "./Mini-Project-2/Largest_banks_data.csv"
read_csv_path = "./Mini-Project-2/exchange_rate.csv"
log_file = "./Mini-Project-2/code_log.txt"

conn = sqlite3.connect(db_name)


def extract(url, table_attribs):
    try:
        html_page = requests.get(url).text
        soup = BeautifulSoup(html_page, "html.parser")
        table = soup.find("table", {"class": "wikitable"})
        data = []

        if table:
            body = table.find("tbody")
            rows = body.find_all("tr")

            for row in rows:
                cols = row.find_all("td")
                if cols:
                    name = cols[1].text.strip()
                    mc = cols[2].text.strip()
                    if name and mc:
                        data.append({table_attribs[0]: name, table_attribs[1]: mc})

            df = pd.DataFrame(data)
            print("Data extracted successfully")
            return df
        else:
            print("Table not found")
            return pd.DataFrame(data)
    except Exception as e:
        print(f"Error in extract function: {e}")
        return pd.DataFrame(data)


def transform(df, read_csv_path):
    try:
        exchange_rate_df = pd.read_csv(read_csv_path)
        exchange_rate_df = exchange_rate_df.set_index('Currency')['Rate']  # Set 'Currency' as index for easy lookup

        df["MC_GBP_Billion"] = round(df["MC_USD_Billion"].astype(float) * exchange_rate_df.get('GBP', 1.0), 2)
        df["MC_EUR_Billion"] = round(df["MC_USD_Billion"].astype(float) * exchange_rate_df.get('EUR', 1.0), 2)
        df["MC_INR_Billion"] = round(df["MC_USD_Billion"].astype(float) * exchange_rate_df.get('INR', 1.0), 2)
        return df
    except Exception as e:
        print(f"Error in transform function: {e}")
        return pd.DataFrame()


def load_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print("Data loaded to CSV successfully")
    except Exception as e:
        print(f"Error in load_to_csv function: {e}")


def load_to_db(df, sql_connection, table_name):
    try:
        df.to_sql(table_name, sql_connection, if_exists="replace", index=False)
        print("Data loaded to DB successfully")
    except sqlite3.Error as e:
        print(f"Error loading to DB: {e}")
    finally:
        if "conn" in locals():
            conn.close()


def run_query(query_statement, sql_connection):
    try:
        query_output = pd.read_sql(query_statement, sql_connection)
        print(query_statement)
        print(query_output)
    except sqlite3.Error as e:
        print(f"Error running query: {e}")
    finally:
        if "conn" in locals():
            conn.close()


def log_progress(message):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + "," + message + "\n")


# Log the initialization of the ETL process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data = extract(url, table_attribs)

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data, read_csv_path)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_to_csv(transformed_data, csv_path)
load_to_db(transformed_data, conn, table_name)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")

# Query the database
run_query("SELECT * FROM Largest_banks;", conn)
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks;", conn)
run_query("SELECT Name from Largest_banks LIMIT 5;", conn)

conn.close()
