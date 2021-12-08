import datetime
from pprint import pprint
from pymongo import MongoClient


def get_database():
    # client = MongoClient("localhost", 27017)
    client = MongoClient("mongodb://dbuser:Pass1234@127.0.0.1:27017/openassetmanagerdb")
    
    return client.openassetmanagerdb


if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

    print(dbname)
    col = dbname.asset_collection
    post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
    # post_id = col.insert_one(post).inserted_id
    # print(post_id)
    print(dbname.list_collection_names())
    for doc in col.find({"author": "Mike"}):
        pprint(doc)