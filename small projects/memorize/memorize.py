import pymongo
import random
import time

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client["Melih"]
collection = db["Words"]


one_frequency = 24*60*60
two_frequency = one_frequency*3
three_frequency = one_frequency*7

one_level = 0
two_level = 2
three_level = two_level + 3

level_one = collection.find_one("levels")['level_one']
level_two = collection.find_one("levels")['level_two']
level_three = collection.find_one("levels")['level_three']



def update():
    collection.update_one({"_id": "levels"}, {"$set":{"level_one":level_one}})
    collection.update_one({"_id": "levels"}, {"$set":{"level_two":level_two}})
    collection.update_one({"_id": "levels"}, {"$set":{"level_three":level_three}})

def addNew(word, meaning):
    level_one.append([word,[meaning, 0, time.time()]])
    update()
    

def quiz():
    random.shuffle(level_one)
    random.shuffle(level_three)
    random.shuffle(level_two)
    for i in range(len(level_one)):
        if level_one[i][1][2]>one_frequency:
            answer = input(level_one[i][0]+": ")
            if answer == "y" or answer == level_one[i][1][0]:
                level_one[i][1][1] += 1
            else:
                level_one[i][1][1] = 0
            level_one[i][1][2] = time.time()
    for i in range(len(level_two)):
        if level_two[i][1][2]>two_frequency:
            answer = input(level_two[i][0]+": ")
            if answer == "y" or answer == level_two[i][1][0]:
                level_two[i][1][1] += 1
            else:
                level_two[i][1][1] = 0
            level_two[i][1][2] = time.time()
    for i in range(len(level_three)):
        if level_three[i][1][2]>three_frequency:
            answer = input(level_three[i][0]+": ")
            if answer == "y" or answer == level_three[i][1][0]:
                level_three[i][1][1] += 1
            else:
                level_three[i][1][1] = 0
            level_three[i][1][2] = time.time()
    update()

def moveToLevel(power, currentLevel, position):
    pass


eval(input())