from pymongo.mongo_client import MongoClient
import pandas as pd
import json


uri = "mongodb+srv://karthik:lpokji00@cluster.ed5uueu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

DATA_FILE_PATH = (r"C:\project\ML-project\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns : {df.shape}")

    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION].insert_many(json_record)