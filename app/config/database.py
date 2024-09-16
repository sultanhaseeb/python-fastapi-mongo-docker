from pymongo import MongoClient

client = MongoClient("mongodb+srv://haseebsultan:ywIv99xynb30uoR1@cluster0.fuklc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.todo_db
collection_name = db["todo_collection"]