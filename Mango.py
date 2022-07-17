import pymongo

client = pymongo.MongoClient("mongodb+srv://root:Amrut2599@amrutop.yg9fncw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)