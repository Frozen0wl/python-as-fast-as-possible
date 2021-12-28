import pymongo
import random
import time
import bisect

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["Melih"]
collection = db["Words"]

id = "levels"

words = collection.find_one(id)['words']

level_one = 0
level_two = 3
level_three = 5

level_one_frequency = 10
level_two_frequency = level_one_frequency*3
level_three_frequency = level_one_frequency*7

listOfLevels = [[level_one, level_one_frequency], [level_two, level_two_frequency], [level_three, level_three_frequency]]
intervals = [level_one, level_two, level_three]

def update():
    collection.update_one({"_id": id}, {"$set": {'words':words}})

def addNewWord(word, meaning):
    #TODO check if the word already exists
    words[word]=[meaning, 0, time.time()]
    update()

def removeWord(word):
    del words[word]
    update()

def shuffle():
    global words
    l = list(words.items())
    random.shuffle(l)
    words = dict(l)

def getInterval(streak):
    i = bisect.bisect_right(intervals, streak)
    return intervals[i-1]

def quiz():
    
    for j in range(0, len(listOfLevels)):
        shuffle()
        item = listOfLevels[j]
        
        print("level", j+1) # prints the current level
        for key, value in words.items():
            if getInterval(value[1]) == item[0] and time.time()-value[2] >= item[1]:
                answer = input(key+": ")
                if answer == value[0] or answer == 'y':
                    words[key][1] += 1 # increase the streak
                else:
                    words[key][1] = 0 # resets the streak
                words[key][2] = time.time() #resets the time
                update()

                    
                

            
eval(input("input: "))




