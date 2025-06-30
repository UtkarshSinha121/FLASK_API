import os
from dotenv import load_dotenv
from pymongo import MongoClient

class Config:
    load_dotenv(".env")
    MONGO_URI = os.getenv("MONGO_URI")

    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client.get_default_database()
