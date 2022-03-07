# Create Event Grid and Topic  

This exercise, we are going to create an Event Grid and Topic. 

1. Create an Event Grid Topic in Azure Portal. Be sure to copy/paste your subscription id and topic endpoint URL (shown below). You will use that later in your Functions app.

![image-event-grid](/images/EventGrid-mytopic1.PNG)

2. Create a new Azure Function, but this time, instead of using the *HTTP Trigger* template, select the *Event Grid Trigger* template.  
3. For the output bindings, we want the binding to export as HTTP response.  
4. Now let's go back to your Event Topic and click on **Create an Event Subscription**.  
5. Give your event subscription a name.  Leave the event grid schema as default.  
6. Select `Event Grid Topic`  as Topic Type.  
7. For end point type, select the Azure Function Event Grid Trigger you have created in step 2.  (You might need to push your changes to Azure Functions from your local machine up into Azure for the Event Subscription, in order to find your recently created Event Grid Trigger.)  
8. Test your app in Postman:
  - Create a POST request with the topic endpoint you copied earlier, e.g.:
```bash
https://{mytopic1}.{eastus-1}.eventgrid.azure.net/api/events  
```
  - In the body, insert the following.  **Replace the subscription-id, resource-group, and topic name with your own names you created earlier**.
```json
[
   {   "id": "01",   
       "eventType": "recordInserted",   
       "subject": "myapp/notes/1",   
       "eventTime": "2020-08-10T21:03:07+00:00",   
       "data": {     
                  "title":"testing title",     
                  "description": "testing description here"   
                },  
        "dataVersion": "1.0",   
        "metadataVersion": "1",   
        "topic": "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.EventGrid/topics/{topic}" 
   }
]
```
  - In the header of the request, make sure you put in the authentication key value pair:  
    - Key Name: aeg-sas-key
    - Value: Your Event Topic's **Access keys** from the Azure Portal
  - If successful, you should get a `Status:200` returned.

9. Lastly, view your Azure Function to see if Event Grid is set up.  You should be able to view your Azure Function log.
