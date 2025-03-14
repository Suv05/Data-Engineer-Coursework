import glob
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

# log file
log_file = "./ETL Basic/log_file.txt"
# to store the final output data that you can load to a database
target_file = "./ETL Basic/transformed_data.csv"


# data extraction from csv file
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


# data extraction from json file
def extract_from_json(file_to_process):
    # extra argument lines=True to enable the function to read the file as a JSON object on line to line basis as follows.
    df = pd.read_json(file_to_process, lines=True)
    return df


# data extraction from xml file
def extract_from_xml(file_to_process):
    df_list = []  # Use a list instead of direct concatenation
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        df_list.append({"name": name, "height": height, "weight": weight})

    return (
        pd.DataFrame(df_list)
        if df_list
        else pd.DataFrame(columns=["name", "height", "weight"])
    )


# extract function basis on file type
def extract():
    extracted_data = []

    for csvfile in glob.glob("./ETL Basic/*.csv"):
        if csvfile != target_file:
            df = extract_from_csv(csvfile)
            if not df.empty:
                extracted_data.append(df)

    for jsonfile in glob.glob("./ETL Basic/*.json"):
        df = extract_from_json(jsonfile)
        if not df.empty:
            extracted_data.append(df)

    for xmlfile in glob.glob("./ETL Basic/*.xml"):
        df = extract_from_xml(xmlfile)
        if not df.empty:
            extracted_data.append(df)

    return (
        pd.concat(extracted_data, ignore_index=True)
        if extracted_data
        else pd.DataFrame(columns=["name", "height", "weight"])
    )


def transform(data):
    """Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters"""
    data["height"] = round(data.height * 0.0254, 2)

    """Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms """
    data["weight"] = round(data.weight * 0.45359237, 2)

    return data


def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)


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
extracted_data = extract()

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")

# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
