import pymongo

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

username = input("Enter username: ").replace(" ", "_")
subject = input("Enter a title (example: German or Vocabulary): ")
category = input("Enter a category (example: everyday vocabulary or Math Vocabulary): ")

db = client[username]
collection = db[subject]

collection.insert_one({"_id": category, "words":{}, "days": True, "hours": True, 
"levels":{"one":[0, 3600*20, 1], "two":[3, 3600*24*2.5, 3], "three":[5, 3600*24*6, 7]}})