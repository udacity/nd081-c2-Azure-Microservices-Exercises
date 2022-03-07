# Deploying Your Client App

To deploy a web app client to the app service, first download [this zip file](client.zip) and extract the contents. 

1. Replace the `request_url` variable in the `app.py` with your own server (if you do not still have the server live from the previous exercise, re-publish it).

```python
... [code omitted]

# in client/app.py
@app.route('/')
def home():
    request_url = ""
    response = requests.get(request_url + 'getAllPosts')
    posts = response.json()
    return render_template("index.html", posts=posts)

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main()

...[code omitted]
```

2. Now let's deploy the application to App Service.  

```bash
az login

# go to the root folder of your functions app
cd ~/client

# install dependencies
pipenv install

# get into the pip env shell
pipenv shell

# deploy application to app service
az webapp up --sku F1 -n $APP_NAME --resource-group $RESOURCE_GROUP
```
