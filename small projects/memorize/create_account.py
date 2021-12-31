import pymongo

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

username = input("Enter username: ").replace(" ", "_")
subject = input("Enter a title (example: German): ")
category = input("Enter a category (example: everyday vocabulary): ")

db = client[username]
collection = db[subject]

collection.insert_one({"_id": category, "words":{}, "time":"daily", "levels":{"one":[0, 1]}})