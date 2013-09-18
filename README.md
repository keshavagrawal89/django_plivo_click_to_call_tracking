django_click_to_call
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
