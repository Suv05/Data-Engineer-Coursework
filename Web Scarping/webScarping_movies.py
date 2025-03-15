import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = "./Web Scarping/Movies.db"
table_name = "Top_50"
csv_path = "./Web Scarping/top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank", "Film", "Year", "Rotten Tomatoes' Top 100"])
count = 0

html_page = requests.get(url).text
soup = BeautifulSoup(html_page, "html.parser")

tables = soup.find_all("tbody")
rows = tables[0].find_all("tr")

for row in rows:
    if count < 50:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {
                # used strip to remove trailing and leading white spaces.
                "Average Rank": col[0].text.strip(),
                "Film": col[1].text.strip(),
                "Year": col[2].text.strip(),
                "Rotten Tomatoes' Top 100": col[3].text.strip() + "🍅",
            }

            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

print(df)
df.to_csv(csv_path)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists="replace", index=False)

# querying
print("querying table")
# query_statement = f"SELECT * FROM {table_name}"
query_statement = f"SELECT * FROM {table_name} WHERE `Average Rank`<=25 LIMIT 25"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
conn.close()
