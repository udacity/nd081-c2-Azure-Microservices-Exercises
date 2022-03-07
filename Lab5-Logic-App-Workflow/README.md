# Logic App Workflow

With Azure Logic Apps and the SendGrid connector, you can automate tasks and workflows that send emails. In this exercise, you'll utilize SendGrid with the Logic App Designer to be able to send emails when an RSS feed is updated.

1. Create a SendGrid Account [here](https://sendgrid.com/). You can use the free service in this exercise, which is enough for our purposes.
2. Login and generate a SendGrid Key.
    - Your API key is located [here](https://app.sendgrid.com/settings/api_keys).
    - Save it down and keep it safe, since that will be used to send emails later on. You will only see this once. 
3. Next, you'll use the Logic App Designer with an RSS feed.
    - Login to the [Azure Portal](https://portal.azure.com).
    - Go to Resources and create a Logic App. 
    - Select Blank Logic Apps template.
    - In the search box, search for "rss". Select RSS.
4. Use the test RSS feed `http://rss.cnn.com/rss/cnn_us.rss` to watch for changes.  You are welcome to use other feeds, if desired. Ideally, you want a news or other busy site that has a frequently updated feed for testing purposes.
    - Fill in the missing to/from and body fields for the email. Ideally, you want to send yourself the feed updates.  
5. Then, click on **New step** and configure your SendGrid email.  Add a new connection using the API key from earlier.  
6. Fill in the missing to/from and body fields for the email. For the subject, write "test from logic app designer", or whatever subject you would like. You could use a throwaway email or send it to your email account to test.

![img-logic-app](/images/test-logic-app.png)

5. You might need to wait 3-5 mins, depending on what RSS feed you chose. Check your inbox to see whether you have appropriately begun receiving emails from SendGrid.






