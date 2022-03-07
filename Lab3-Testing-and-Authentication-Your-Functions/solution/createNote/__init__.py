import azure.functions as func
import pymongo


def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = ""
            client = pymongo.MongoClient(url)

            database = client['mytestdb']
            collection = database['notes']

            collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)
    else:

        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400)
