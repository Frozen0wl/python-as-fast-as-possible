import pymongo
import random
import time
import bisect
import datetime
import artikel2
import reminder_email

client = pymongo.MongoClient("mongodb+srv://main:main@memorizecluster.guleg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["Melih"]
collection = db["Words"]

i = 0
for item in collection.find():
    i+=1

if i > 1:
    id = input(" | ".join([item["_id"] for item in collection.find()])+": ")
else:
    id = [item["_id"] for item in collection.find()][0]
    print(id)

try:
    words = collection.find_one(id)['words']
except:
    print("invalid input")
    quit()


levels = collection.find_one(id)['levels']

listOfLevels = [levels["one"], levels["two"], levels["three"]]

intervals = [levels["one"][0], levels["two"][0], levels["three"][0]]

days = collection.find_one(id)['days']
hours = collection.find_one(id)['hours']

def copyWordsToAnotherCategory(category):
    targetCategory = collection[category]
    dic_1 = targetCategory['words']
    newDic = dic_1.items()+words.items()
    collection.update_one({"_id": category}, {"$set": {'words':newDic}})

def stages():
    pass

def update():
    collection.update_one({"_id": id}, {"$set": {'words':words}})
    
def addMultipleWords():
    while True:
        addNewWord(input("word: "), input("meaning: "))

def addNewWord(word, meaning):
    for key in words:
        if key == word:
            print("The word is already in your list")
            return
    words[word]=[meaning, 0, time.time(), 0, str(datetime.date.today())] # answer, streak, time, total number of guesses, todays date
    update()

def addArticle(word):
    word = word.capitalize()
    try:
        artikel = artikel2.getArticle(word)
        addNewWord(word, artikel)
    except:
        print("The word doesn't exist!")
    
def addMultipleArticles():
    while True:
        word = input("word: ").capitalize()
        addArticle(word)
        try:
            print(words[word][0]) # prints the article
        except:
            pass

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
    dash = '-' * 53
    i=0
    j=0
    for key in words:
        
        if i == 0:
            print(dash)
            print('{:<10s}{:>23s}{:>10s}{:>10s}'.format("word","meaning","streak","time"))
            print(dash)
            i += 1
        j+=1
        print('{:<20s}{:>13s}{:>8d}{:>11.1f}h'.format(str(j)+". "+key,words[key][0],words[key][1], (time.time()-words[key][2])/3600))

def quiz():    
    for j in range(0, len(listOfLevels)):
        shuffle()
        item = listOfLevels[j]
        
        print("level", j+1) # prints the current level
        for key, value in words.items():
            if getInterval(value[1]) == item[0] and ((time.time()-value[2] >= item[1] and hours) or ((datetime.datetime.today()-datetime.datetime.strptime(value[4], '%Y-%m-%d')).days >= item[2] and days)):
                answer = input(key+": ")
                if answer == value[0] or answer == 'y':
                    words[key][1] += 1 # increase the streak
                else:
                    words[key][1] = 0 # resets the streak
                    print(f'the correct answer was: {value[0]}')
                words[key][2] = time.time() #resets the time
                words[key][3] += 1
                words[key][4] = str(datetime.date.today())
                update()


eval(input("input: "))




