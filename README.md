linkedin_wrapper
================

Python wrapper to LinkedIn authentication API.

It was a pain to get LinkedIn authentication running with my Python web app, so I decided to make it simpler for everyone else. Here's a Python wrapper to authorizing LinkedIn profiles with your application. 

To generate authentication token in your app, execute the following code: 

from flask import request
import linkedin_wrapper

li = linkedin_wrapper.LinkedIn()
url = li.get_authorization_code()
#authorize linkedin profile
token = li.generate_app(request.args.get('code'))



Explanation 
================

Send user to following URL. 

>> url = li.get_authorization_code()

After the user signs into the application, get authorization code. Successful authentication redirects application to RETURN_URL?code=TOKEN. For example, you can do that with the following in real time, with the Flask request library (retrieve with pip install Flask-Request). 

>> token = li.generate_app(request.args.get('code'))

Then use the token to get the user's profile.

>> li.get_profile(token)

You can change the field selectors to filter out the info that is returned. More info here: https://developer.linkedin.com/documents/profile-fields