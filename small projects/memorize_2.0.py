import pymongo
import random
import time
import bisect
import datetime

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["Melih"]
collection = db["Words"]


id = input(" | ".join([item["_id"] for item in collection.find()])+": ")

try:
    words = collection.find_one(id)['words']
except:
    print("invalid input")
    quit()

level_one = 0
level_two = 3
level_three = 5

day = 3600*24

level_one_frequency = day-3600
level_two_frequency = day*2.5
level_three_frequency = day*6

listOfLevels = [[level_one, level_one_frequency], [level_two, level_two_frequency], [level_three, level_three_frequency]]
intervals = [level_one, level_two, level_three]


def update():
    collection.update_one({"_id": id}, {"$set": {'words':words}})

def addMultipleWords():
    while True:
        addNewWord(input("word: "), input("meaning: "))

def addNewWord(word, meaning):
    for key in words:
        if key == word:
            print("word already exists")
            return
    words[word]=[meaning, 0, time.time(), 0] # answer, streak, time, total number of guesses
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

def printWords():
    dash = '-' * 48
    i=0

    for key in words:
        
        if i == 0:
            print(dash)
            print('{:<10s}{:>18s}{:>10s}{:>10s}'.format("word","meaning","streak","time"))
            print(dash)
            i += 1

        print('{:<15s}{:>13s}{:>8d}{:>11.1f}h'.format(key,words[key][0],words[key][1], (time.time()-words[key][2])/3600))

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
                    print(f'the correct answer was: {value[0]}')
                words[key][2] = time.time() #resets the time
                words[key][3] += 1
                update()

       

eval(input("input: "))




