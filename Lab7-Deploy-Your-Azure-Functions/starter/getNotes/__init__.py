import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = ""
        client = pymongo.MongoClient(url)
        database = ""
        collection = ""


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        return func.HttpResponse("Could not connect to mongodb",
                                 status_code=400)

