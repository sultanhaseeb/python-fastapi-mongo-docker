from pymongo import MongoClient

client = MongoClient(
    "past-db-connectio-string"
)
db = client.user
collection_name = db["users"]
