from bson.objectid import ObjectId
import pymongo



client = pymongo.MongoClient("mongodb+srv://Admin:powerpoint@chahae-in.l0naw.mongodb.net/?retryWrites=true&w=majority")

test = {
    "testKey3": {"key":"value", "key2":"value2"},
    "testKey4": "testValue2",
    "testKey5": "testValue3"
}


with client:
    db = client.test
    collection = db["er"]
    collection.update_one({"_id":ObjectId("607af1fe72c29d287f07c8d4")}, {"$set": test}, upsert = True)
                
    data = db["er"].find_one(ObjectId("607af1fe72c29d287f07c8d4"))
    
    print(data["testKey3"])