django_plivo_click_to_call_tracking
====================

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

![alt tag](https://www.evernote.com/shard/s160/sh/23127c7e-1d43-40ba-b7d3-6e1f8a5aa44a/0e73b63f961fbfbda049c80341cc2c95/deep/0/Screenshot%209/21/13%203:47%20AM.jpg)

![alt tag] (https://www.evernote.com/shard/s160/sh/0346c435-ef00-438b-a868-54878baad50c/c1a67a518a920b978767a15530eb59ea/deep/0/Screenshot%209/21/13%203:46%20AM.jpg)

Notice '/manage_lead/' under urls.py

![alt tag] (https://www.evernote.com/shard/s160/sh/b3d286f7-2bc5-4f61-b0e0-16300c947065/3c97a2af2d1510e6448734e23212b06a/deep/0/Screenshot%209/21/13%203:50%20AM.jpg)
Cheers!
