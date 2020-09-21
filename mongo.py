import pymongo
import os
if os.path.exists("env.py"):
  import env 

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "sample_airbnb"
COLLECTION_NAME = "listingsAndReviews"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find() 
total_count = coll.count_documents({}) 

# for doc in documents:
#     print(doc)

print(total_count)


