import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ["MyDbConnection"] # Change the Variable name, as applicable to you
        client = pymongo.MongoClient(url)
        database = client['lab2db'] # Change the MongoDB name
        collection = database['notes']    # Change the collection name


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except ConnectionError:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

