# Lab7 - Deploy Your Azure Functions

If your app is still ready to go from before with the related database still live, deploying an Azure function is fairly straightforward.

If the database is no longer live, you can go back to the "Serverless Functions" lesson and follow the steps to set up the CosmosDB account and MongoDB database again, along with loading sample information into the database. From there, you can use the files [here](https://video.udacity-data.com/topher/2020/June/5ed6f7af_getnotes/getnotes.zip) along with the necessary connection and collection information for `__init__.py` to be ready to deploy.

1. Deploy your `getNotes` endpoint to a live server, instead of localhost:7071.

```bash
# the app name is the name of your function app 
func azure functionapp publish <APP_NAME>
```

2. The result should give you a live URL in this format:

```bash
Functions in <APP_NAME>:
    getNotes - [httpTrigger]
        Invoke url: https://<APP_NAME>.azurewebsites.net/api/getNotes
```

3. Visit the URL given back to you and confirm that you are able to access the API appropriately on the live website.
