import datetime
import pymongo

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["Melih"]
collection = db["test"]

class word:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.streak = 0
        self.totalGuess = 0
        self.insertionDate = datetime.datetime.now()
    
    def returnDic():
        pass
mouse = word("mouse", "maus")
print(type(mouse).__name__)
