from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:********@cluster0.conab68.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]
