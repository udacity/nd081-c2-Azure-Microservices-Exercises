 # Create CosmosDB Service to Work with Azure Functions
 
In this exercise, you will create more functions you would expect from a servicing API.

### Database Creation and Connecting the Database to Azure Functions

1. **Create CosmosDB account**: First, create a CosmosDB account with MongoDB to store our collections in the database. 


2. **Create MongoDB database**: Next, create a MongoDB database and `notes` collection within that database, using `sample_db.json` (download [here](https://video.udacity-data.com/topher/2020/June/5ed6dbf4_sample-db/sample-db.json)) to populate it with some sample values. 


3. **Create Functions**: In your VSCode Editor, right click on the Azure Functions. You can select the last function we were working with. Azure will ask for the resource group and storage account and language. Select HTTPTrigger template. You will need two function endpoints - one for `getNotes` (all notes) and one for `getNote` (just a single note).


4. **Edit Functions**: Edit the function `init.py` for each function endpoint. You need to use the correct mongodb method to call and grab all the collection `notes` items.



5. **Run the Functions**: Lastly, serve your function to localhost, and check if you can obtain the related sample information through your browser.
