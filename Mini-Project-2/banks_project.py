import pandas as pd
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes = ["Name", "MC_USD_Billion"] #upon extraction only
table_attributes_final = [
    "Name",
    "MC_USD_Billion",
    "MC_GBP_Billion",
    "MC_EUR_Billion",
    "MC_INR_Billion",
]

db_name = "./Mini-Project-2/Banks.db"
table_name="Largest_banks"
csv_path = "./Mini-Project-2/Largest_banks_data.csv"
log_file = "./Mini-Project-2/code_log.txt"