# Importing python dependencies
import pymongo

# Initializing mongodb
mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)
db = client["TODO"]
collection = db['todo']


# CRUD operations
def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def getAll():
    response = collection.find({})
    data = []
    for i in response:
        i['_id'] = str(i["_id"])
        data.append(i)
    return data

def getTask(condition):
    response = collection.find_one({"name":condition})
    response["_id"] = str(response["_id"])
    return response

def update(name,data):
    data = dict(data)
    response = collection.update_one({"name":name},{"$set":data})
    return response.modified_count

def delete(name):
    response = collection.delete_one({"name":name})
    return response.deleted_count