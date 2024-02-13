import pymongo
#from mongoDB no sql database

con = pymongo.MongoClient("mongodb://localhost:27017")
db = con["univ"]
collection = db["students"]

result = collection.find({"marks":{"$gt":92}})
for std in result:
    print(std["name"])
    print(std["major"])
    print(std["marks"])

