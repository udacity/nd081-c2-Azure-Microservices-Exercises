# Lab1 - Creating your First Function on the Portal

In this lab, you will create your first Azure Functions straight from the terminal. You will not use Python (since it is not supported in the portal), but instead will select either C# or nodeJS language to generate your function.

The purpose is not to get hung up on languages per se, but to see the structure of a function app and be familiar with the necessary files, such as:

- function.json and its purpose
- local.settings.json and its purpose
- and the code file(s) to work on

You will need very minimal editing to the function. By then end, you will deploy and preview your function app on a live url!

### Part 1

1. Create a new resource group.
2. Create a new Function App. Make sure your resource group is the same resource group you have created in the first step.
3. Once the function app is created, click on "add a new function". For example, in the below image, I've created a function app called "udacitydemodotnet".

![lab3-img1](/images/lab3-img1.PNG)  

4. Launch your function as HTTPFunction template. Select "anonymous" as authLevel.
5. Once it is launched, copy/paste the test function url. For example mine is:
    ```bash
    http://udacitydemodotnet.azurewebsites.net/api/MyFirstHttpFunction
    ```
    By default, the HTTPTrigger template has a "name" parameter. Put your name in the url function (append like so):
    ```bash
    http://udacitydemodotnet.azurewebsites.net/api/MyFirstHttpFunction?name=your-name-here
    ```

You should see a "Hello, {your-name-here}" message back in the browser.

Congratulations, you just created your first Azure Function! Let's continue.


### Part 2

Suppose I only want the function to take in the `get` method and not any other method. What would you change in the `function.json` configuration file?

```json
{
  "bindings": [
    {
      "authLevel": "anonymous",
      "name": "req",
      "type": "httpTrigger",
      "direction": "in",
      "methods": [
        "get",
        "post"
      ]
    },
    {
      "name": "$return",
      "type": "http",
      "direction": "out"
    }
  ]
}
```

- Change the `bindings` `type` from `httpTrigger`.
- Add a `get` method.
- Remove the `"post"` from `methods`.
- This is not possible.

Answer: You got it, you will need to remove the "post" method.

```bash
{
  "bindings": [
    {
      "authLevel": "anonymous",
      "name": "req",
      "type": "httpTrigger",
      "direction": "in",
      "methods": [
        "get"
      ]
    },
    {
      "name": "$return",
      "type": "http",
      "direction": "out"
    }
  ]
}
```

### Part 3

Here, you'll create a customized key/value variable in the Application Settings.

To do so, go to your application settings and add a new variable called `MyDBConnectionString` as the key.  For the value, just write `"placeholderstring"` for now - we don't have a database yet!

### Part 4

Let's replicate our HTTPTrigger function, but with Python and the Azure CLI.  

Most of the Portal is great for testing out services, or to obtain keys or configuration files.  For actual development, it would be more practical to use the command line to create our functions.   Let's go into our Azure CLI and replicate what we did earlier.  This time, instead of choosing a .Net Function App, create a new app and select Python.  

Python is still in an experimental phase and is not supported on the Portal just yet. However, for the remainder of the course, we will develop in the Python programming language using the CLI, which does support Python.  

1. On your machine, use the below command to create a new function.  Call the function app name a variation of "MyTestAPI", perhaps with some numbers added to the end so you have a custom app name.
  - Replace the resource group and storage account variable with your own variable.  For region, select US West or US East.  Other regions might not fully support the Python language yet, so only select one of these two. If you don't know your storage account name, go to your resource group in the portal and it will list it for you.  

  ```bash
  echo "Create a empty function app on Linux (Consumption Plan): $APP_NAME"
  az functionapp create \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --storage-account $STORAGE_ACCOUNT \
    --os-type Linux \
    --consumption-plan-location $REGION \
    --runtime python
  ```

  2. Now create your HTTP Function:
  ```bash
  func new --language python --name MyHTTPFunction
  ```

#### Common Pitfalls:
1. Receiving the following error when creating a function app in the terminal:  "The requested app service plan cannot be created in the current resource group because it is hosting Linux apps. Please choose a different resource group or create a new one."
  - **Resolution:** Create another resource group and make sure that no other function apps are using it. Your resource group would also require a new storage account.  
2. Receiving the error: "Website with given name MyTestAPI already exists".  
  - **Resolution:** App names must be unique, so append your `MyTestAPI` with some number such as `MyTestAPI12345` to see if it works.
  ```bash
  az functionapp create \
    --resource-group labRG \
    --os-type linux \
    --consumption-plan-location EastUS \
    --storage-account mylabstorage000 \
    --runtime python \
    --name MyTestAPI000
  ```
