# Lab 6 - Azure Functions with Trigger Notification
 
 In this exercise, you'll add an output binding for Twilio's SendGrid mail notification whenever there is an HTTP input trigger. 

 1. Make sure you have extensions installed for SendGrid bindings in your `host.json` from the last exercise:

 ```json
 {
   "version": "2.0",
   "extensionBundle": {
     "id": "Microsoft.Azure.Functions.ExtensionBundle",
     "version": "[1.*, 2.0.0)"
   },
   "extensions": {
     "sendGrid": {
         "from": "Azure Functions <samples@functions.com>"
     }
   }
 }
 ```

 2. Create a [SendGrid](https://sendgrid.com/) free account (if you don't already have one) and obtain the the token. You will need these for the output bindings later. You also need to use an email as a verified sender. You may want to read more about [Single Sender Verification](https://sendgrid.com/docs/for-developers/sending-email/sender-identity/#single-sender-verification).
 3. Append the SendGrid output binding to your `host.json` file.
 4. By default all SendGrid functions must be admin level functions.  You will need to add **x-functions-key** and an access key for the header.  
 5. Create your sendGrid call. For further reference on the SendGrid class, view the [SendGrid Python repo](https://github.com/sendgrid/sendgrid-python/). You can pass a serialized JSON object to the `func.Out` parameter to send to your email.
