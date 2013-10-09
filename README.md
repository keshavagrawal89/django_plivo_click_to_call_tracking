django_plivo_click_to_call_tracking
====================

Django Version: 1.5

Nothing fancy.

Just plain django project.

1. Copy Paste the whole project
2. Change the db settings in settings.py
3. Change th auth_id and auth_token in settings.py
4. Check other details in urls.py and you are good to go.

====================

This will present a text box and a submit button. User can enter their number and press "Click Me".

1. Agent's number configured gets the call.
2. He hears some text notification that he is going to be connected with some visitor
3. Customter/user gets the call on the number entered in the textbox
4. They both get connected
5. At the end of the call 'from'(User/Customer) number, 'to'(Agent number) and Duration of the call is stored in the DB. 
6. This data can be easily used to draw a quick graph using so many graph JavaScripts available. And that will help to get some statistics.
7. With this current project data is stored in the db withh table name "Lead" (Check models.py)

====================

This is just to show how data can be pulled from the db and reflected on a graph. Notice '/track_lead/' under urls.py

![alt tag](https://www.evernote.com/shard/s160/sh/2f330658-764a-434d-aabe-c47f441feaed/269c4eb3c02cd95bd4fef09c6389b984/deep/0/Screenshot%209/21/13%203:36%20PM.jpg)

Notice the "Send Report" button
![alt tag] (https://dl.dropboxusercontent.com/u/54579287/Screenshot-4.png)

Change FROM_EMAIL, TO_EMAIL and other constants in settings.py file according to your mailgun details to receive email.
Notice '/manage_lead/' under urls.py

![alt tag] (https://www.evernote.com/shard/s160/sh/b3d286f7-2bc5-4f61-b0e0-16300c947065/3c97a2af2d1510e6448734e23212b06a/deep/0/Screenshot%209/21/13%203:50%20AM.jpg)
Cheers!
