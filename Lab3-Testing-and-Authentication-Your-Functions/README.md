# Testing and Authentication Your Functions  

In this exercise, you will test your functions locally with Postman, as well as adding basic authentication for securing your functions.

### Part 1: Testing

1. Now that you have created your functions, serve them locally (if you haven't already).
  ```bash
  func start
  ```
  - Make sure you have installed the appropriate dependencies, or else `func start` will throw an error.
  - You should see your two functions, `getNote` and `getNotes`, served at the localhost:7071/api/ route.

2. Go to your Postman app (or [download it](https://www.postman.com/downloads/) if you don't have it yet) and test out the first function using the same route.
3. Create another function called `createNote` and repeat the same set up process as for the previous exercise. You will need to complete the missing pieces on the below starter code for the `__init__.py` file:

```python
import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = ""
            client = pymongo.MongoClient(url)

            # you will need this fill in
            database = ""
            collection = ""

            # replace the insert_one variable with what you think should be in the bracket
            collection.insert_one([WHAT-SHOULD-GO-IN-HERE})

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )
```

4. You will also need to update the `function.json` file, which is missing a request type. What should this be for `methods`?
```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "connectionStringSetting": "",
      "methods": []
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

5. Restart your function locally so it includes your updates.
6. Go back to Postman and select the POST request. Set the request body option as JSON format. Add in this sample body:
```json
{ "title" : "My first note", "description: "My first note from POSTMAN request"}
```
7. Try one of the GET requests again within Postman to check that the new note was correctly added.

### Part 2: Authentication

#### Function-Level

Azure Functions allow you to shield unauthorized requests by means of authorization keys. Each function has multiple "authorization levels":  
- `anonymous` means no API key, everybody can access your endpoint
- `function` means an API key is required (this is what we are getting)
- `host keys` that allow an admin to access all functions in a single function app  
    
1. Change the `function.json` "authLevel" property from "anonymous" to "function."  This means you have added an extra layer of security to the `createNote` endpoint. Only users with access keys can access.  
2. Grab the Functions Keys in your Dashboard > Function App > [YOUR_FUNCTION_APP_NAME]. Copy/paste the value of the key named "default".  It should be called *default* key.  
3. Now for the GET request url like step 4 of **Testing** above, you would need to add the extra `?code="your-default-key-here"` at the end of your function in the url. If you do not provide this, you will not have access to the endpoint. 
```bash
# The format
https://localhost:8000/api/<FUNCTION_NAME>?code=<API_KEY>
```

4. Test that you can make successful request while using the default key in the request url parameter.

#### App-Level

1. Next, instead of using a `function`-level key, let's switch to a `master` key so we can access the entire function. For the POST request with host key access, copy/paste the *master* key from the portal (as shown below).

![function-host-keys](https://docs.microsoft.com/en-us/azure/azure-functions/media/functions-manually-run-non-http/azure-portal-functions-master-key.png)

2. Change your `function.json` "authLevel" property to "admin".
3. In the header of the POST request object, add **x-functions-key** as a key and paste your saved default functions key as the value.
