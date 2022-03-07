# Containerizing Your Apps for AKS

In this exercise, you'll containerize your app with Docker and then deploy it with Kubernetes, which would be very helpful for scaling up your app deployment.

### Part 1: Create a Container Registry

1. First, make sure you have [Docker](https://www.docker.com/get-started) installed.
2. Create the container registry.

```bash
RESOURCE_GROUP="<your-resource-group-name>"
APP_REGISTRY="<create-name-for-your-app-registry>"

az acr create --resource-group $RESOURCE_GROUP --name $APP_REGISTRY --sku Basic
```

3. Login to your registry that you just created. Azure will ask for username and password. This is under your Container Registry service >> Settings >> Access Keys.

```bash
docker login <name-of-your-registry-on-azure>
```

### Part 2: Containerize the App

1. Create a Dockerfile.
```bash
func init --docker-only
```
2. Build the docker image.
```bash
docker build -t <your-image-name>
```
3. Test the image locally.
```bash
docker run -p 8080:80 -it <your-image-name>
```
4. Tag your docker image for Azure Container Registry.
```bash
docker tag <your-image-name> <your-registry-name>.azurecr.io/<your-image-name>
```
5. Push the image to Azure Container Registry.
```bash
docker push <your-registry-name>.azurecr.io/<your-image-name>
```

### Part 3: Create a Kubernetes Cluster

1. First, make sure you have the Kubernetes command line tool `kubectl` installed as per the instructions [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
2. Create a Kubernetes cluster on Azure:

```bash
az aks create \
    --resource-group $RESOURCE_GROUP \
    --name $APP_REGISTRY \
    --node-count 1 \
    --enable-addons monitoring \
    --generate-ssh-keys
```
This should return a JSON object with your AKS deployment information.

3. Now, get your credentials for AKS.

```bash
# you should already have these made
RESOURCE_GROUP="<your-resource-group>"
FUNCTIONS_CLUSTER="<your-functions-cluster"

# Get credentials
az aks get-credentials --name $FUNCTIONS_CLUSTER --resource-group $RESOURCE_GROUP
```

4. Verify the connection to your cluster with the command:
```bash
kubectl get nodes
```

Example output:
```bash
NAME                                STATUS   ROLES   AGE    VERSION
aks-nodepool1-38515171-vmss000000   Ready    agent   3m2s   v1.15.10
```

### Part 4: Deploy the App to Kubernetes

1. Deploy the function app to your container registry.

```bash
APP_NAME="<YOUR_FUNCTION_APP_NAME>"
REGISTRY_NAME="<YOUR_AZURE_CONTAINER_REGISTRY_NAME>"

func deploy 
     --platform kubernetes 
     --name $APP_NAME
     --registry $REGISTRY_NAME
```

2. Check your deployment:

```bash
kubectl config get-contexts
```
