import sqlite3
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
db_name = "./Mini-Project-1/World_Economy.db"
table_name = "Countries_by_GDP"
csv_path = "./Mini-Project-1/Countries_by_GDP.csv"
table_attributes = ["Country", "GDP_USD_MILLIONS"]
df = pd.DataFrame(columns=table_attributes)
log_file = "./Mini-Project-1/etl_project_log.txt"
conn = sqlite3.connect(db_name)  # conn made


def extract(url, table_attributes):
    try:
        html_page = requests.get(url).text
        soup = BeautifulSoup(html_page, "html.parser")
        table = soup.find("table", {"class": "wikitable"})  # Find table by class

        if table:
            rows = table.find_all("tr")
            data = []

            for row in rows[1:]:  # Skip header row
                cols = row.find_all("td")
                if len(cols) >= 3:  # check if the row has enough columns
                    country = cols[0].text.strip()
                    gdp = cols[2].text.strip()
                    if country and gdp:  # check if the extracted data is not empty.
                        data.append(
                            {table_attributes[0]: country, table_attributes[1]: gdp}
                        )
            df = pd.DataFrame(data)
            print("Data extracted successfully")
            return df
        else:
            print("Table not found")
            return pd.DataFrame(columns=table_attributes)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return pd.DataFrame(columns=table_attributes)
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return pd.DataFrame(columns=table_attributes)


def transformed(df):
    # Replace "—" with NaN
    df["GDP_USD_MILLIONS"] = df["GDP_USD_MILLIONS"].replace("—", np.nan)

    # Remove commas and convert to float
    df["GDP_USD_MILLIONS"] = df["GDP_USD_MILLIONS"].str.replace(",", "")
    df["GDP_USD_MILLIONS"] = df["GDP_USD_MILLIONS"].astype(float)

    # Divide and round
    df["GDP_USD_BILLIONS"] = round(df["GDP_USD_MILLIONS"] / 1000, 2)
    print("Data transformed successfully")
    return df


def load_to_csv(df, csv_path):
    df_to_save = df[["Country", "GDP_USD_BILLIONS"]]  # Select only the desired columns
    df_to_save.to_csv(csv_path, index=False)
    print("Data loaded to CSV successfully")


def load_to_db(df, db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)

        # Select only the desired columns
        df_to_load = df[["Country", "GDP_USD_BILLIONS"]]
        df_to_load.to_sql(table_name, conn, if_exists="replace", index=False)
        print("Data loaded to DB successfully")
    except sqlite3.Error as e:
        print(f"Error loading to DB: {e}")
    finally:
        if "conn" in locals():
            conn.close()


def run_query(query_statement, sql_conn):
    query_output = pd.read_sql(query_statement, sql_conn)
    print(query_statement)
    print(query_output)


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
extracted_data = extract(url, table_attributes)

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transformed(extracted_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_to_csv(transformed_data, csv_path)
load_to_db(transformed_data, db_name, table_name)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")

# Query the database
query_statement = "SELECT * FROM Countries_by_GDP"
run_query(query_statement, conn)

conn.close()
